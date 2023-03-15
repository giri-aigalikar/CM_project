import sys
#import clr # <- uncomment if you are running a National Instruments Project

sys.path.append("C:/IPG/carmaker/win64-10.2.2/Python")
from ASAM.XIL.Implementation.Testbench import TestbenchFactory
from ASAM.XIL.Interfaces.Testbench.MAPort.Enum.MAPortState import MAPortState
from ASAM.XIL.Interfaces.Testbench.Common.Error.TestbenchPortException import TestbenchPortException

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

        # Start CarMaker instance using a MAPortConfig .xml file
        DemoMAPortConfig = DemoMAPort.LoadConfiguration(MAPortConfigFile)
        DemoMAPort.Configure(DemoMAPortConfig, False)

        # Configure Variables to capture
        print("Creating capture with FileWriter...")
        DemoCapture = DemoMAPort.CreateCapture("captureTask")
        DemoVariableList = ["Car.ax", "Car.ay", "Car.az", "DM.Steer.Ang"]
        DemoCapture.Variables = DemoVariableList
        DemoCapture.Downsampling = 50
        # create mdffilewriter
        DemoCaptureWriter = MyCapturingFactory.CreateCaptureResultMDFWriterByFileName("MDFFile")

        # set capture with conditions
        print("Adding Start and StopTrigger...")
        StartDelay = MyDurationFactory.CreateTimeSpanDuration(-2.0)
        DemoStartWatcher = MyWatcherFactory.CreateDurationWatcherByTimeSpan(10.0)
        DemoCapture.SetStartTrigger(DemoStartWatcher, StartDelay)
        DemoStopWatcher = MyWatcherFactory.CreateDurationWatcherByTimeSpan(20.0)
        StopDelay = MyDurationFactory.CreateTimeSpanDuration(2.0)
        DemoCapture.SetStopTrigger(DemoStopWatcher, StopDelay)
        DemoCapture.Start(DemoCaptureWriter)

        print("Starting simulation...")
        # start the testrun
        if DemoMAPort.State is not MAPortState.eSIMULATION_RUNNING:
            DemoMAPort.StartSimulation("Examples/BasicFunctions/Driver/BackAndForth")

        DemoMAPort.WaitForSimEnd(120.0)
        print("Simulation finished. MDF File saved to: " + DemoMAPort.Configuration.Project + "/MDFFile.mf4")

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
