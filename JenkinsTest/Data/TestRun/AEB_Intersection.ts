#INFOFILE1.1 - Do not remove this line!
FileIdent = CarMaker-TestSeries 10
FileCreator = CarMaker 10.2.2
Description:
	"The TestSeries including the cross traffic TestRuns. "
	The Series shows the speedvariation of vut and traffic object.
	The start position of the traffic object is set via the script file.
LastChange = 2022-09-22 13:20:06 giri.aigalikar
StartTime = 2022-09-22 13:16:39
EndTime = 2022-09-22 13:16:43
ReportTemplate =
Step.0 = Settings
Step.0.Name = Global Settings
Step.0.Param.0 = ScriptFile CM Scripts/Intersection.tcl
Step.0.Param.1 = StartProc CM MyStartProc
Step.1 = TestRun
Step.1.Name = Examples/DriverAssistance/BrakingAssist/AEB_CrossingCarIntersection
Step.1.Param.0 = Speed_vut NValue
Step.1.Param.1 = Speed_TO NValue
Step.1.Crit.0.Name = Collision Detection
Step.1.Crit.0.Description:
Step.1.Crit.0.Good =
Step.1.Crit.0.Warn =
Step.1.Crit.0.Bad = [get Sensor.Collision.Vhcl.Fr1.Count] > 0
Step.1.Var.0.Name = Variation 0
Step.1.Var.0.Param = 40 10
Step.1.Var.0.Result = good
Step.1.Var.0.ResDate = 1663866894
Step.1.Var.0.ResFiles = SimOutput/131452.erg
Step.1.Var.0.ManLst = 0
Step.1.Var.0.Crit.0.Name = Collision Detection
Step.1.Var.0.Crit.0.Result = good
Step.1.Var.1.Name = Variation 1
Step.1.Var.1.Param = 45 10
Step.1.Var.1.Result = err
Step.1.Var.1.ResDate = 1663866898
Step.1.Var.1.ResFiles = SimOutput/131456.erg
Step.1.Var.1.ManLst = 0
Step.1.Var.1.Log.0.Time = 15.832
Step.1.Var.1.Log.0.Kind = err
Step.1.Var.1.Log.0.Text = Simulation stopped by user
Step.1.Var.2.Name = Variation 2
Step.1.Var.2.Param = 50 10
Step.1.Var.2.Result = good
Step.1.Var.2.ResDate = 1663866779
Step.1.Var.2.ResFiles = SimOutput/131257.erg
Step.1.Var.2.ManLst = 0
Step.1.Var.2.Crit.0.Name = Collision Detection
Step.1.Var.2.Crit.0.Result = good
Step.1.Var.3.Name = Variation 3
Step.1.Var.3.Param = 40 40
Step.1.Var.3.Result = bad
Step.1.Var.3.ResDate = 1663867003
Step.1.Var.3.ResFiles = SimOutput/131641.erg
Step.1.Var.3.ManLst = 0
Step.1.Var.3.Crit.0.Name = Collision Detection
Step.1.Var.3.Crit.0.Result = bad
Step.1.Var.4.Name = Variation 4
Step.1.Var.4.Param = 45 40
Step.1.Var.4.Result = bad
Step.1.Var.4.ResDate = 1663866786
Step.1.Var.4.ResFiles = SimOutput/131305.erg
Step.1.Var.4.ManLst = 0
Step.1.Var.4.Crit.0.Name = Collision Detection
Step.1.Var.4.Crit.0.Result = bad
Step.1.Var.5.Name = Variation 5
Step.1.Var.5.Param = 50 40
Step.1.Var.5.Result = bad
Step.1.Var.5.ResDate = 1663866790
Step.1.Var.5.ResFiles = SimOutput/131308.erg
Step.1.Var.5.ManLst = 0
Step.1.Var.5.Crit.0.Name = Collision Detection
Step.1.Var.5.Crit.0.Result = bad
Step.2 = TestRun
Step.2.Name = Examples/DriverAssistance/BrakingAssist/AEB_CrossingCyclistIntersection
Step.2.Param.0 = Speed_vut NValue
Step.2.Param.1 = Speed_TO NValue
Step.2.Crit.0.Name = Collision Detection
Step.2.Crit.0.Description:
Step.2.Crit.0.Good =
Step.2.Crit.0.Warn =
Step.2.Crit.0.Bad = [get Sensor.Collision.Vhcl.Fr1.Count] > 0
Step.2.Var.0.Name = Variation 0
Step.2.Var.0.Param = 40 10
Step.2.Var.0.Result = good
Step.2.Var.0.ResDate = 1663866794
Step.2.Var.0.ResFiles = SimOutput/131312.erg
Step.2.Var.0.ManLst = 0
Step.2.Var.0.Crit.0.Name = Collision Detection
Step.2.Var.0.Crit.0.Result = good
Step.2.Var.1.Name = Variation 1
Step.2.Var.1.Param = 45 10
Step.2.Var.2.Name = Variation 2
Step.2.Var.2.Param = 50 10
Step.2.Var.2.Result = good
Step.2.Var.2.ResDate = 1663866147
Step.2.Var.2.ResFiles = SimOutput/130226.erg
Step.2.Var.2.ManLst = 0
Step.2.Var.2.Crit.0.Name = Collision Detection
Step.2.Var.2.Crit.0.Result = good
Step.2.Var.3.Name = Variation 3
Step.2.Var.3.Param = 40 15
Step.2.Var.3.Result = good
Step.2.Var.3.ResDate = 1663866151
Step.2.Var.3.ResFiles = SimOutput/130229.erg
Step.2.Var.3.ManLst = 0
Step.2.Var.3.Crit.0.Name = Collision Detection
Step.2.Var.3.Crit.0.Result = good
Step.2.Var.4.Name = Variation 4
Step.2.Var.4.Param = 45 15
Step.2.Var.4.Result = good
Step.2.Var.4.ResDate = 1663866155
Step.2.Var.4.ResFiles = SimOutput/130233.erg
Step.2.Var.4.ManLst = 0
Step.2.Var.4.Crit.0.Name = Collision Detection
Step.2.Var.4.Crit.0.Result = good
Step.2.Var.5.Name = Variation 5
Step.2.Var.5.Param = 50 15
Step.2.Var.5.Result = good
Step.2.Var.5.ResDate = 1663866158
Step.2.Var.5.ResFiles = SimOutput/130237.erg
Step.2.Var.5.ManLst = 0
Step.2.Var.5.Crit.0.Name = Collision Detection
Step.2.Var.5.Crit.0.Result = good
TS.Speed_TO = 15
TS.TO_Length = 2
