from os import path
from config.setup import _setup;

def main():
    '''Starts program execution.'''
    
    # FETCHING NEEDED DEPENDENCIES
    ROOT_DIRECTORY = path.realpath(path.join(path.dirname(__file__)));
    REQUIREMENTS_FILE_PATH = "./requirements.txt";
    _setup(path.join(ROOT_DIRECTORY, REQUIREMENTS_FILE_PATH));
    
    
if __name__ == "__main__":
    main();