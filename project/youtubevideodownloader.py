  
#Downloading Single Video
# Install pytube library by using command "pip install pytube3"

from pytube import YouTube
import os

def downloadYouTube(videourl, path):
    try:
        yt = YouTube(videourl)
    except:
        print("Connection Error")
   #This will help in selcting highest quality video    
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    try:
        yt.download(path)
    except:
        print("Download Not finished!")
    print("Download Successful! Check out the downloaded videos in Downloads.")

    
def main():
    link=input("Enter the link:")
    downloadYouTube(link, './Downloads')
    
main()