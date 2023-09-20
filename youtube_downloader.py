from pytube import YouTube
import ffmpeg
import os

path = os.path.abspath(os.getcwd())
path = path + "\\"

#progressive streams have the video and audio 
#in a single file, but typically 
#do not provide the highest quality media 

#adaptive streams split the video and audio 
#tracks but can provide much higher quality

def changeTitle(vtitle):
    
    title = str(vtitle)

    title = title.replace('/','')
    title = title.replace('.','')
    title = title.replace('?','')

    return title

def renameFile(vtitle, num):

    vtitle = str(changeTitle(vtitle))

    if num == 1:
        current_file_name = vtitle + '.mp4'
        new_file_name = vtitle + '_v.mp4'
    elif num == 2:
        current_file_name = vtitle + '.mp4'
        new_file_name = vtitle + '_s.mp3'

    try:
        os.rename(current_file_name, new_file_name)
    except FileNotFoundError:
        print(f"File '{current_file_name}' not found.")
    except FileExistsError:
        print(f"File '{new_file_name}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

def downloadVideoPart(vres):
    l1 = list(yt.streams.filter(res=vres).itag_index)
    idx = l1[0]
    v_stream = yt.streams.get_by_itag(idx)
    v_stream.download()

    renameFile(v_stream.title, 1)
    title = changeTitle(v_stream.title)
    mergeFiles(title)
    
def downloadAudioPart():
    l2 = list(yt.streams.filter(only_audio=True).itag_index)
    if 140 in l2:
        a_stream = yt.streams.get_by_itag(140)
        a_stream.download()
    else:
        idx = l2[0]
        a_stream = yt.streams.get_by_itag(idx)
        a_stream.download()

    renameFile(a_stream.title, 2)

def mergeFiles(title):
    video_input = ffmpeg.input(path + f'{title}_v.mp4')
    audio_input = ffmpeg.input(path + f'{title}_s.mp3')

    output_file = path + f'{title}.mp4'

    ffmpeg.output(video_input, audio_input, output_file, vcodec='copy', acodec='aac').run()

print("Welcome to YouTube video/audio downloader by berkay2756!")
num = 0
while num not in [1, 2, 3]:
    num = int(input("\nInputs: \n1: Download video (mp4)\n2: Download audio only (mp3)\n3: Exit program\nYour choice: "))

if num == 3:
    input("\nPress Enter to continue...")
else:
    url = str(input("Enter the URL of the video: "))
    yt = YouTube(url)

    if num == 1:

        vres = str(input("Select the quality of the video (Quality above 240p is supported): "))
        downloadAudioPart()
        downloadVideoPart(vres)

        vtitle = str(changeTitle(yt.title))
        vtitle2 = vtitle + "_s.mp3"
        vtitle = vtitle + "_v.mp4"

        os.remove(vtitle)
        os.remove(vtitle2)

    elif num == 2:
        downloadAudioPart()

    input("\nPress Enter to continue...")