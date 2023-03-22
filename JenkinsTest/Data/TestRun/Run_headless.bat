FOR %%i IN (..\..\Startupfiles\*.*) DO (..\..\src\CarMaker.win64.exe %%i -v -screen -dstore)
cd ../../
move SimOutput C:\Users\giri.aigalikar\Desktop
