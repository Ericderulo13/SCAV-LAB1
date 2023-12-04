#imports
from PIL import Image
import numpy as np
import subprocess
import matplotlib.pyplot as plt
import numpy as np

#Exercice 1
class lab3():

    def macroblocks_motionVectors(self,video):
      result1 = subprocess.run([f'ffmpeg -flags2 +export_mvs -i {video} -vf codecview=mv=pf+bf+bb  motion_vectors_video.mp4'],shell=True, stdout=subprocess.PIPE, text=True)

    #Exercice 2
    def containers_creation_50_sec(self,video):
      result = subprocess.run(["ffmpeg"], stdout=subprocess.PIPE, text=True)
      result1 = subprocess.run([f'ffmpeg -i bbb.mp4 -ss 00:00:00 -t 00:00:50 -c:v copy -c:a copy bbb50.mp4'], shell=True,stdout=subprocess.PIPE, text=True)
      result2 = subprocess.run([f"ffmpeg -i bbb50.mp4 -vn -acodec libmp3lame -ac 1 mp3_audio_mono.mp3"],shell=True, stdout=subprocess.PIPE, text=True)
      result3 = subprocess.run([f"ffmpeg -i bbb50.mp4  -vn -acodec libmp3lame -b:a 32k -ac 2 mp3_audio_stereo.mp3"],shell=True, stdout=subprocess.PIPE, text=True)
      result4= subprocess.run([f"ffmpeg -i bbb50.mp4 -vn -c:a aac video_audio.aac"],shell=True, stdout=subprocess.PIPE, text=True)
      unpacking =subprocess.run(["ffmpeg -i bbb50.mp4 -i mp3_audio_mono.mp3 -i mp3_audio_stereo.mp3 -i video_audio.aac -map 0:v -map 1:a -map 2:a -map 3:a container_video.mp4"],shell = True ,stdout=subprocess.PIPE, text=True)

    #Exercice 3
    def showing_tracks_containers(self,video):
      # Run the 'ffmpeg' command to check if it's installed
        result = subprocess.run(["ffmpeg"], stdout=subprocess.PIPE, text=True)
        # Run the 'ffprobe' command to get information about the video
        result1 = subprocess.run([f"ffprobe -v error -select_streams a -show_entries stream=index -of default=nokey=1:noprint_wrappers=1 {video}"], shell=True,stdout=subprocess.PIPE, text=True)
        audio_tracks = result1.stdout.strip().split('\n')

        # Count the number of audio tracks
        num_audio_tracks = len(audio_tracks)

        return num_audio_tracks



if __name__ == "__main__":
    import subtiles_script as sub
    import yuv_histogram_script as yuv
    result = subprocess.run(["ffmpeg"], stdout=subprocess.PIPE, text=True)
    result1 = subprocess.run([f'ffmpeg -i bbb.mp4 -ss 00:00:00 -t 00:00:09 -c:v copy -c:a copy bbb9.mp4'],shell=True, stdout=subprocess.PIPE, text=True)
    var = lab3()
    #Exercici 1
    var.macroblocks_motionVectors("bbb9.mp4")
    #Exercici 2
    var.containers_creation_50_sec("bbb.mp4")
    #Exercici 3
    print("Number of audio tracks",var.showing_tracks_containers("container_video.mp4"))
    # Exercici 4 + 5.
    sub.subtitles().subtitles_performing("bbb9.mp4","eric.srt")
    # Exercici 6
    yuv.yuvi().yuv_histogram("bbb9.mp4")