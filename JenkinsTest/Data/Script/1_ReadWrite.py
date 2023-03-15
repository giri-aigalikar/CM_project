import sys
#import clr # <- uncomment if you are running a National Instruments Project

sys.path.append("C:/IPG/carmaker/win64-10.2.2/Python")
from ASAM.XIL.Implementation.Testbench import TestbenchFactory
from ASAM.XIL.Interfaces.Testbench.MAPort.Enum.MAPortState import MAPortState
from ASAM.XIL.Interfaces.Testbench.Common.Error.TestbenchPortException import TestbenchPortException

MAPortConfigFile = "Config.xml"

if __name__ == "__main__":
    DemoMAPort = None

    try:
        # Initialize all necessary class instances
        MyTestbenchFactory = TestbenchFactory()
        MyTestbench = MyTestbenchFactory.CreateVendorSpecificTestBench("IPG", "CarMaker", "10.2.2")
        MyMAPortFactory = MyTestbench.MAPortFactory
        MyWatcherFactory = MyTestbench.WatcherFactory

        print("Creating and Configuring MAPort...")
        DemoMAPort = MyMAPortFactory.CreateMAPort("DemoMAPort")

        # Start CarMaker instance using a Project directory as Configuration parameter
        DemoMAPortConfig = DemoMAPort.LoadConfiguration(MAPortConfigFile)
        DemoMAPort.Configure(DemoMAPortConfig, False)

        print("Starting simulation...")
        if DemoMAPort.State is not MAPortState.eSIMULATION_RUNNING:
            DemoMAPort.StartSimulation("Examples/BasicFunctions/Driver/BackAndForth")

        # Overwrite the Steering angle during simulation at different times
        DemoMAPort.WaitForTime(10.0, 30.0)
        # change steering angle
        print("SteerAng after 10s: " + str(DemoMAPort.Read("DM.Steer.Ang")))
        print("Setting steer angle to 1 rad for 100ms")
        DemoMAPort.Write("DM.Steer.Ang", 1.0, 100)
        DemoMAPort.WaitForTime(10.1, 30.0)
        print("New SteerAngle after write: " + str(DemoMAPort.Read("DM.Steer.Ang")))

        DemoMAPort.WaitForTime(20.0, 30.0)
        # change steering angle without pause
        print("SteerAngle after 20s: " + str(DemoMAPort.Read("DM.Steer.Ang")))
        print("Setting steer angle to -2 rad for 100ms")
        DemoMAPort.Write("DM.Steer.Ang", -2.0, 100)
        DemoMAPort.WaitForTime(20.1, 30.0)
        print("New steering angle after write: " + str(DemoMAPort.Read("DM.Steer.Ang")))

        # Stop simulation
        DemoMAPort.StopSimulation()

    except TestbenchPortException as ex:
        print("TestbenchPortException occured:")
        print("VendorCodeDescription: %s" % ex.VendorCodeDescription)

    finally:
        if DemoMAPort != None:
            DemoMAPort.Dispose()
            DemoMAPort = None
