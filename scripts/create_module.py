import os # work with file system
import sys # read the arguments from command line.

# read module name from command line argument
"""
Ex:- python create_module.py user
This will create:['create_module.py','user']
user is the module name
if arguments are not passed it will throw an index error and script will crash.
"""
module_name = sys.argv[1]
print(module_name)

# get the current working directory
BASE_DIR = os.getcwd()

# define paths for each file
paths = {
    "controller": f"{BASE_DIR}/controllers/{module_name}_controller.py",
    "route": f"{BASE_DIR}/routes/{module_name}_routes.py",
    "model": f"{BASE_DIR}/models/{module_name}.py",
    "test": f"{BASE_DIR}/test_case/test_{module_name}.py",
}

#  create files if they do not exist
# iterate the loop for each file path
for file_path in paths.values():
    if not os.path.exists(file_path): # check if file already exists and if does not exist create it
        open(file_path, "w").close()
        print(f"Created: {file_path}")
    else: # if file exists and print already exists
        print(f"Already exists: {file_path}")

# register the routes in the main routes file







