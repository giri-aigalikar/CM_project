import sys
#import clr # <- uncomment if you are running a National Instruments Project

sys.path.append("C:/IPG/carmaker/win64-10.2.2/Python")
from ASAM.XIL.Implementation.Testbench import TestbenchFactory
from ASAM.XIL.Interfaces.Testbench.MAPort.Enum.MAPortState import MAPortState
from ASAM.XIL.Interfaces.Testbench.Common.Error.TestbenchPortException import TestbenchPortException
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
        MyWatcherFactory = MyTestbench.WatcherFactory
        MyDurationFactory = MyTestbench.DurationFactory

        print("Creating and Configuring MAPort...")
        DemoMAPort = MyMAPortFactory.CreateMAPort("DemoMAPort")

        # Start CarMaker instance using a Project directory as Configuration parameter
        DemoMAPortConfig = DemoMAPort.LoadConfiguration(MAPortConfigFile)
        DemoMAPort.Configure(DemoMAPortConfig, False)

        # Configure a capture with a DurationWatcher
        # to stop the capturing after 10 seconds
        print("Creating capture...")
        DemoCapture = DemoMAPort.CreateCapture("capture")
        DemoVariableList = ["Car.ax", "Car.ay", "Car.az", "DM.Steer.Ang"]
        DemoCapture.Variables = DemoVariableList
        DemoCapture.Downsampling = 20

        # ConditionWatcher Definition
        print("Adding Condition Start and StopTriggers...")
        StartDelay = MyDurationFactory.CreateTimeSpanDuration(-2.0)
        DemoStartWatcher = MyWatcherFactory.CreateConditionWatcher("Car.ay > 1.5")
        DemoCapture.SetStartTrigger(DemoStartWatcher, StartDelay)
        StopDelay = MyDurationFactory.CreateTimeSpanDuration(2.0)
        DemoStopWatcher = MyWatcherFactory.CreateConditionWatcher("Car.ay < -1.5")
        DemoCapture.SetStopTrigger(DemoStopWatcher, StopDelay)

        # Activate capture before simstart
        DemoCapture.Start()

        # Start the simulation
        print("Starting simulation...")
        if DemoMAPort.State is not MAPortState.eSIMULATION_RUNNING:
            DemoMAPort.StartSimulation("Examples/BasicFunctions/Driver/ChangingLanes")

        # Wait for the trigger to stop the capture
        # this is signaled by passing 'True' to the Fetch call
        print("Waiting for StopCondition...")
        Result = DemoCapture.Fetch(True)
        # Stop the simulation after capture is stopped
        DemoMAPort.StopSimulation()
        print("Simulation finished. Saving result to " + DemoMAPort.Configuration.Project + "/mygraph.png")

        # Visualization of capture result using matplotlib
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
        # save figure to file
        plt.savefig('mygraph.png')

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
