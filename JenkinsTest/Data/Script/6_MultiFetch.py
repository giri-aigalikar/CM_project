import sys
#import clr # <- uncomment if you are running a National Instruments Project

sys.path.append("C:/IPG/carmaker/win64-10.2.2/Python")
from ASAM.XIL.Implementation.Testbench import TestbenchFactory
from ASAM.XIL.Interfaces.Testbench.MAPort.Enum.MAPortState import MAPortState
from ASAM.XIL.Interfaces.Testbench.Common.Error.TestbenchPortException import TestbenchPortException
from ASAM.XIL.Interfaces.Testbench.Common.Capturing.Enum.CaptureState import CaptureState
from matplotlib import pyplot as plt

MAPortConfigFile = "Config.xml"

if __name__ == "__main__":
    DemoCapture = None
    DemoMAPort = None

    try:
        # Initialise all necessary class instances
        MyTestbenchFactory = TestbenchFactory()
        MyTestbench = MyTestbenchFactory.CreateVendorSpecificTestBench("IPG", "CarMaker", "10.2.2")
        MyMAPortFactory = MyTestbench.MAPortFactory
        MyCapturingFactory = MyTestbench.CapturingFactory
        MyWatcherFactory = MyTestbench.WatcherFactory
        MyDurationFactory = MyTestbench.DurationFactory

        print("Creating and Configuring MAPort...")
        DemoMAPort = MyMAPortFactory.CreateMAPort("DemoMAPort")

        # Start CarMaker instance using a Project directory as Configuration parameter
        DemoMAPortConfig = DemoMAPort.LoadConfiguration(MAPortConfigFile)
        DemoMAPort.Configure(DemoMAPortConfig, False)

        # Configure Variables to capture
        print("Creating Capture...")
        DemoCapture = DemoMAPort.CreateCapture("captureTask")
        DemoVariableList = ["Time", "Car.ax", "Car.ay", "Car.az", "DM.Steer.Ang"]
        DemoCapture.Variables = DemoVariableList
        DemoCapture.Downsampling = 50
        # Configure Capture conditions
        # Here: capture from 10 to 19 seconds into the simulation
        print("Adding Start and StopTrigger...")
        DemoStartWatcher = MyWatcherFactory.CreateDurationWatcherByTimeSpan(10.0)
        DemoCapture.SetStartTrigger(DemoStartWatcher)
        StopDelay = MyDurationFactory.CreateTimeSpanDuration(-1.0)
        DemoStopWatcher = MyWatcherFactory.CreateDurationWatcherByTimeSpan(20.0)
        DemoCapture.SetStopTrigger(DemoStopWatcher, StopDelay)
        DemoCapture.Start()

        print("Starting simulation...")
        if DemoMAPort.State is not MAPortState.eSIMULATION_RUNNING:
            DemoMAPort.StartSimulation("Examples/BasicFunctions/Driver/BackAndForth")

        # Fetch data multiple times and do something with it
        # here we just save the data to display later
        # capture every second of data between start and end condition
        # set simtime to first second after startcondition is triggered
        simtime = 11.0
        Results = []
        # repeatedly call fetch to get data.
        # CAUTION: avoid processing the data during simulation as this can slow
        # down the capturing process and lead to loss of data
        print("fetching every second...")
        while DemoCapture.State != CaptureState.eFINISHED:
            DemoMAPort.WaitForTime(simtime)
            # save data for postprocessing
            Results.append(DemoCapture.Fetch(False))
            simtime = simtime + 1.0
            # Fetch returns None if Capture hasn't started yet or no data is available
            if Results[-1] is None:
                del Results[-1]
                continue

        # After capture is finished we can call fetch again to get all captured data
        # and then stop the simulation
        finalResult = DemoCapture.Fetch(True)
        DemoMAPort.StopSimulation()
        print("Simulation finished. Results saved in ProjectDir: " + DemoMAPort.Configuration.Project)

        # Plot captured data for every Fetch call or other postprocessing
        count = 0
        for Result in Results:
            XAxisValues = Result.GetSignalGroupValue().XVector.Value

            AccXSignalValue = Result.ExtractSignalValue("Car.ax")
            AccXValues = AccXSignalValue.FcnValues.Value

            AccYSignalValue = Result.ExtractSignalValue("Car.ay")
            AccYValues = AccYSignalValue.FcnValues.Value

            AccZSignalValue = Result.ExtractSignalValue("Car.az")
            AccZValues = AccZSignalValue.FcnValues.Value

            plt.xlabel("Seconds")
            plt.ylabel("m/s^2")
            plt.xlim(min(XAxisValues), max(XAxisValues))
            plt.plot(XAxisValues, AccXValues, 'r')
            plt.plot(XAxisValues, AccYValues, 'g')
            plt.plot(XAxisValues, AccZValues, 'b')
            plt.savefig('graph_' + str(count) + '.png')
            count = count + 1

        # Visualization of capture result using matplotlib
        XAxisValues = finalResult.GetSignalGroupValue().XVector.Value

        AccXSignalValue = finalResult.ExtractSignalValue("Car.ax")
        AccXValues = AccXSignalValue.FcnValues.Value

        AccYSignalValue = finalResult.ExtractSignalValue("Car.ay")
        AccYValues = AccYSignalValue.FcnValues.Value

        AccZSignalValue = finalResult.ExtractSignalValue("Car.az")
        AccZValues = AccZSignalValue.FcnValues.Value

        plt.xlabel("Seconds")
        plt.ylabel("m/s^2")
        plt.xlim(min(XAxisValues), max(XAxisValues))
        plt.plot(XAxisValues, AccXValues, 'r')
        plt.plot(XAxisValues, AccYValues, 'g')
        plt.plot(XAxisValues, AccZValues, 'b')
        plt.savefig('alldata.png')

    except TestbenchPortException as ex:
        print("TestbenchPortException occured:")
        print("VendorCodeDescription: %s" % ex.VendorCodeDescription)

    finally:
        if DemoCapture != None:
            DemoCapture.Dispose()
            DemoCapture = None
        if DemoMAPort != None:
            DemoMAPort.Dispose()
            DemoMAPort = None
