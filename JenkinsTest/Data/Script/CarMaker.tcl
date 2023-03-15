# PROC SimInput::AddQuInfo { }
#
# Define additional entries in Input From file dialog
#
# 4 values needed:  key english_txt german_txt unit
#
#   key    keyname, used as key name in TestRun File.
#          Same name will be used by the simulation program.
#          Pay attention: Only User1, User2, ..., User30 will be 
#          supported by default, other names will need an extension 
#          of the ExternalInputs module(not possible for the user).
#   *_txt  Text shown in dialog (englisch, german)
#   unit   Unit, used only in dialog
#
# Remarks:
# - To add new entries to the dialog you just need to call 
#   the SimInput::AddQuInfo procedure
# - to rearrange or exclude some channels from the list use SimInput::QuList (see below)

 SimInput::ResetUserDef
# foreach {q etxt gtxt unit} {
     SimInput::CreateNewUserDef
     # set SimInput::QuInfo(User1) [l User1 User1]
	 # set TestRun(OW-User1-FileQu) [l User1 User1]
	 SimInput::CreateNewUserDef
     # set SimInput::QuInfo(User2) [l User2 User2]
	 # set TestRun(OW-User2-FileQu) [l User2 User2]
	 SimInput::CreateNewUserDef
	 SimInput::CreateNewUserDef
	 SimInput::CreateNewUserDef
	 SimInput::CreateNewUserDef

	 
 SimInput::UpdateQuTable
