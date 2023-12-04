from PIL import Image
import numpy as np
import subprocess
import json
import  matplotlib.pyplot as plt
#EXERCICI 1

class lab2():

    def video_converting(self,video):
        result = subprocess.run(["ffmpeg"], stdout=subprocess.PIPE, text=True)
        result1 = subprocess.run([f'ffmpeg -i {video} -c:v mpeg2video -b:v 8000k -c:a mp2 -b:a 384k bbb.mpg'],shell=True, stdout=subprocess.PIPE, text=True)
        result2 = subprocess.run(["ffprobe -i bbb.mpg -show_streams -show_format -print_format json -v quiet -of json > video_info.json"],shell=True, stdout=subprocess.PIPE, text=True)

    #Exercici 2
    def resolution_modifying(self,video):
        #Assuming resolution 16:9
        resolution_list=[144,240,360,480,720,1080]
        resolution = int(input("Choose your resoltuion :144,240,360,480,720,1080"))
        while resolution not in resolution_list:
            resolution = int(input("Choose a valid  resoltuion :144,240,360,480,720,1080"))
        width= (resolution/9)*16;
        if isinstance(width,float):
            width= round(width)
        if width % 2 != 0:  # Si la anchura no es divisible por 2
            width +=1
        height= resolution
        result = subprocess.run(["ffmpeg"], stdout=subprocess.PIPE, text=True)
        result1 = subprocess.run([f'ffmpeg -i {video} -vf "scale={width}:{height}" -c:a copy new_bbb_resolution_{resolution}.mp4'],shell=True ,stdout=subprocess.PIPE, text=True)
        return resolution

    #Exercici 3
    def chroma_subsampling(self,video):
        chroma_values=["4:2:0","4:2:2","4:4:4","4:1:1"]
        chroma= str(input("choose your chroma values:4:2:0 4:2:2,4:4:4,4:1:1"))
        while chroma not in chroma_values:
            chroma = str(input("choose a valid chroma values:4:2:0 4:2:2 4:4:4 4:1:1"))
        values = list(map(int, chroma.split(':')))
        luma, h, v = values
        result = subprocess.run(["ffmpeg"], stdout=subprocess.PIPE, text=True)
        result1 = subprocess.run([f'ffmpeg -i {video} -ss 00:00:00 -t 00:00:08 -c:v copy -c:a copy output33.mp4'],shell=True, stdout=subprocess.PIPE, text=True)

        result2 = subprocess.run([f'ffmpeg -i output33.mp4 -vf "format=yuv{luma}{h}{v}p" -c:v libx264 -crf 20 -c:a copy chroma_subsampling.mp4'],shell=True,stdout=subprocess.PIPE, text=True)

    #Exercici 4 print 5 relevant data from the video
    def reading_video_info(self,video_json):
        with open(video_json, "r") as file:
            data = json.load(file)  # Load the entire JSON file
        return data


import P1.main as p1
import P3.LAB3 as p3
if __name__ == "__main__":

#Cutting the video to 30 seconds.
    result = subprocess.run(["ffmpeg"], stdout=subprocess.PIPE, text=True)
    result1 = subprocess.run([f'ffmpeg -i bbb.mp4 -ss 00:00:00 -t 00:00:30 -c:v copy -c:a copy bbb30.mp4'],shell=True, stdout=subprocess.PIPE, text=True)
#Exercicis Executables. On està també l'herència,
    lab2().video_converting("bbb30.mp4")  #Funnciona
    lab2().resolution_modifying("bbb30.mp4") #Funciona
    lab2().chroma_subsampling("bbb.mp4")
    info_video = lab2().reading_video_info("video_info.json")
    if info_video:
        format_info = info_video.get('format', {})
        if format_info:
            print("Format Information:")
            print(f"Bit_rate: {format_info.get('bit_rate')}")
            print(f"Format Name: {format_info.get('format_name')}")
            print(f"Format Long Name: {format_info.get('format_long_name')}")
            print(f"Start Time: {format_info.get('start_time')}")
            print(f"Probe Score: {format_info.get('probe_score')}")

    #Utilitzem la funcion de la pràctica anterior.
    result = subprocess.run(["ffmpeg"], stdout=subprocess.PIPE, text=True)
    result1 = subprocess.run(["ffmpeg -i bbb.mp4 -vf 'fps=1' framechosed.jpg"], shell=True, stdout=subprocess.PIPE,text=True)
    result2 = p1.black_white("framechosed.jpg")
    # Subtitles function from lab3.
    p3.subtitles_performing("bbb30.mp4","eric.srt")
