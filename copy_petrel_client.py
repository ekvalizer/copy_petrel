import os
import glob
from distutils.dir_util import copy_tree


petrel_version = 2019
petrel_env = f"PETREL{petrel_version}"
petrel_dir_path = f"C:\\Petrels\\{petrel_env}"

#create env variable if not exists
if not petrel_env in os.environ:
    os.environ.putenv(petrel_env, petrel_dir_path)    

#make directory for petrel if not exists
if not os.path.isdir(petrel_dir_path):
    os.makedirs(petrel_dir_path)

#get latest petrel from src
petrel_src = r'C:\petrelssrc\\'
latest_petrel_dir = max(glob.glob(os.path.join(petrel_src, '*/')), key=os.path.getmtime)
copy_tree(latest_petrel_dir, petrel_dir_path)
print('Complete!')

