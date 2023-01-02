import argparse;
import os;
import re
import shutil
import sys;
from pytube import YouTube, exceptions;

class Downloader():
    
    def __init__(self) -> None:
        pass
    
    def download_url(self, url:str, mediaFormat:str, outputDir:str , add_author:bool = False):
        # Getting Youtube video.
        try:
            print(f"Loading url...");
            yt = YouTube(url);
            media_stream =yt.streams \
                .filter(type=mediaFormat, progressive=False, file_extension="mp4") \
                .asc() \
                .first()
            
            # Setting name.
            mediaName = yt.title + ".mp4";
            if add_author == True:
                mediaName = f"{yt.author}-{mediaName}"; 
                
            # Downloading
            print(f"Downloading {yt.title}...");
            media_stream.download(output_path=outputDir, filename=mediaName);
            
        except exceptions.RegexMatchError:
            print("This URL does not point to any Youtube video...")
    
    def download_url_from_file ():
        pass;
    
    def getURLSFromFile(self, filename:str) -> list[str]:
        urls = []
        with open(filename, "r") as file:
            for url in file:
                url = url.rstrip()
                if url != "" and self.is_youtube_like_url(url):
                    urls.append(url);
        return urls;
    
    def is_youtube_like_url(self, url:str) -> bool:
        '''Check if a given string follows a youtube like url pattern.'''
        if re.match(r"\Ahttps:\/\/www.youtube.com\n*|\Ahttps:\/\/youtu.be\/", url) != None:
            return True;
        return False;
    
def display_progress_bar(
    bytes_received: int, filesize: int, ch: str = "█", scale: float = 0.55
) -> None:
    """Display a simple, pretty progress bar.
    Example:
    ~~~~~~~~
    PSY - GANGNAM STYLE(강남스타일) MV.mp4
    ↳ |███████████████████████████████████████| 100.0%
    :param int bytes_received:
        The delta between the total file size (bytes) and bytes already
        written to disk.
    :param int filesize:
        File size of the media stream in bytes.
    :param str ch:
        Character to use for presenting progress segment.
    :param float scale:
        Scale multiplier to reduce progress bar size.
    """
    columns = shutil.get_terminal_size().columns
    max_width = int(columns * scale)

    filled = int(round(max_width * bytes_received / float(filesize)))
    remaining = max_width - filled
    progress_bar = ch * filled + " " * remaining
    percent = round(100.0 * bytes_received / float(filesize), 1)
    text = f" ↳ |{progress_bar}| {percent}%\r"
    sys.stdout.write(text)
    sys.stdout.flush()

if __name__ == "__main__":
    a = Downloader(None);
    print(a.getURLSFromFile(os.path.dirname(__file__) + "/../a.txt"))
    print(a.is_youtube_like_url("https://youtu.be/ZsvftkbbrR0"));