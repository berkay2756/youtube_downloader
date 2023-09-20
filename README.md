# youtube_downloader
A program for extracting video and audio from YouTube videos.

This program is built on Python and uses these libraries:
- pytube
- ffmeg

pytube is used for getting the YouTube video and its properties.

For creating a mp4 file, the program gets audio and video parts of the video 
separately and then they are combined using ffmpeg. This process results in
higher quality than getting audio and video together.

For creating a mp3, file, the program simply retrieves the audio part of the
video and converts it into a mp3 file (audio is retrieved as a mp4 file).
