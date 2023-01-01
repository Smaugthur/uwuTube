import pkg_resources    # Functionalities to check project requirements.
from pkg_resources import DistributionNotFound
from os import path, _exit
import sys
import subprocess

def _setup(REQUIREMENTS_FILE_PATH:str):
    """
    This function checks if the user has all dependencies installed. 
        If not, it just stop the execution of the WHOLE program.
    """
    dependencies = getDependencies(REQUIREMENTS_FILE_PATH);
    
    try:
        pkg_resources.require(dependencies)

    except DistributionNotFound:
        try :
            opcion = input("\nMISSING DEPENDENCIES: Install them?\nYes[y], No[n]:")
            if opcion == 'y':
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r' , REQUIREMENTS_FILE_PATH]) # <- download the dependencies.
                input("\n\n\tINSTALLATION FINISHED. press <Enter> to continue...\n")
            elif opcion == 'n':
                print("Aborting installation...")
                _exit(1)
            else:
                print("No valid option, aborting installation.")
                _exit(1)
        except:
            print("Pip seems not to be installed, try executing the following command:\n\n\tpython -m ensurepip --upgrade")
            _exit(1)
            
def getDependencies(REQUIREMENTS_FILE_PATH:str) -> list[str]:
    '''Returns a list of each of the needed libraries listed in REQUIREMENTS_FILE_PATH file.'''
    dependencies = []
    if (path.isfile(REQUIREMENTS_FILE_PATH)):
        with open (REQUIREMENTS_FILE_PATH, "r") as modules_depedencies:
            for modules in modules_depedencies:
                dependencies.append(modules.rstrip());
    return dependencies;