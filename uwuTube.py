from sys import exit;
from os import mkdir;
from os import path
from config.setup import _setup;
import argparse;
from src.Downloader import Downloader;

def main():
    '''Command line application to download youtube videos.'''
    
    # FETCHING NEEDED DEPENDENCIES
    ROOT_DIRECTORY = path.realpath(path.join(path.dirname(__file__)));
    REQUIREMENTS_FILE_PATH = "./requirements.txt";
    _setup(path.join(ROOT_DIRECTORY, REQUIREMENTS_FILE_PATH));
    
    # FETCHING ARGUMENTS FROM CLI (argparser object)
    parser = argparse.ArgumentParser(description=main.__doc__)
    args = getArgs(parser);
    
    # CREATING DIR IF DOES NOT EXIST YET.
    if args.outputDir != None and path.isdir(args.outputDir) == False:
        create_dir(args.outputDir);
        
    # DOWNLOADING MEDIA FOR EACH ENTRY.
    yt_downloader = Downloader()
    for entry in args.URLS:
        if(path.isfile(entry)):
            pass
        else:
            yt_downloader.download_url(
                entry,
                args.format,
                args.outputDir,
                args.AddAuthors
            )

    
def getArgs(parser: argparse.ArgumentParser) -> argparse.Namespace:
    '''Configure the given parser and returns a list of arguments passed by the user.'''
    parser.add_argument("URLS",
                        type=str,
                        nargs="+",
                        help="URL or List of Youtube URL's to download.");
    parser.add_argument("-o",
                        "--outputDir",
                        type=str,
                        default="./",
                        required=False,
                        help="Set the destination to all the downloaded media.");
    parser.add_argument("-f",
                        "--format",
                        type=str,
                        choices=["audio", "video", "both"],
                        default="audio",
                        required=False,
                        help="Set the media format to be downloaded (only audio, video or both)");
    parser.add_argument("-a",
                        "--AddAuthors",
                        type=str,
                        nargs="?",
                        const=True,
                        default=False,
                        required=False,
                        help="Adds the author name before the media name, when saving on your system. Example: Daft Punk-Voyager.mp3");
    return parser.parse_args();

def create_dir(dir_path:str):
    '''Creates a dir if a given path is valid.'''
    try: 
        mkdir(dir_path);
    except:
        print("Incorrect path for dir.");
        exit(1);
    
if __name__ == "__main__":
    main();