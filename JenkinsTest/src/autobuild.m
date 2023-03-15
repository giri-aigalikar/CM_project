setenv('MSYS_ROOT' , 'MSYS-2020')
addpath(genpath('C:/Users/giri.aigalikar/Desktop/Git_Clone/test-repo1/JenkinsTest/src'));
load_system('BrakeJenkins');
set_param('BrakeJenkins','LaunchReport','off');
try
	rtwbuild('BrakeJenkins');
catch
	warning('Error while building Model1');
% 	exit(1);
end
save_system('BrakeJenkins');
close_system('BrakeJenkins');
