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

        print("Creating and Configuring MAPort...")
        DemoMAPort = MyMAPortFactory.CreateMAPort("DemoMAPort")

        # Start CarMaker instance using a Project directory as Configuration parameter
        DemoMAPortConfig = DemoMAPort.LoadConfiguration(MAPortConfigFile)
        DemoMAPort.Configure(DemoMAPortConfig, False)

        # Configure Variables to capture
        print("Creating capture...")
        DemoCapture = DemoMAPort.CreateCapture("captureTask")
        DemoVariableList = ["Car.ax", "Car.ay", "Car.az"]
        DemoCapture.Variables = DemoVariableList
        DemoCapture.Downsampling = 50

        # run a couple of TestRuns and capture acceleration data
        TestRuns = ["Examples/BasicFunctions/Driver/BackAndForth",
        	    "Examples/VehicleDynamics/Braking/Braking"]
        i = 0
        for testrun in TestRuns:
            # capture data once the testrun starts
            print("Activate capture...")
            DemoCapture.Start()

            print("Starting simulation...")
            # start the testrun
            if DemoMAPort.State is not MAPortState.eSIMULATION_RUNNING:
                DemoMAPort.StartSimulation(testrun)

            # Wait for the simulation to end and get the CaptureResult
            print("Waiting for simend and retrieving data...")
            DemoMAPort.WaitForSimEnd(120.0)
            Result = DemoCapture.Fetch(False)
            DemoCapture.Stop()
            print("Simulation finished. Saving result to " + DemoMAPort.Configuration.Project + f"/graph_{i}.png.")

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
            plt.savefig(f'graph_{i}.png')
            # or show figure on screen
            # plt.show()
            plt.clf()
            i = i+1

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
