import os
import subprocess

env_var = "PETRELBUILD2019"
env_val = "\"C:\\Users\\OSergeev\\OneDrive - Schlumberger\\Desktop\\gohfer\\srv complete\""
str = f"SETX {env_var} {env_val} /M"
os.system(str)

#subprocess.call(['runas', '/user:Administrator', 'SETX {0} {1} /M".format(env_var,env_val)'])
print('Complete!')