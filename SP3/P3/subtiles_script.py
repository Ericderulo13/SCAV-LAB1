from PIL import Image
import numpy as np
import subprocess
import  matplotlib.pyplot as plt
import numpy as np

class subtitles():
    # Exercice 4
    def subtitles_performing(self,video,subtitles,output_path):
        result = subprocess.run(["ffmpeg"], stdout=subprocess.PIPE, text=True)
        result1 = subprocess.run([f'ffmpeg -i {video} -vf "subtitles={subtitles}" -c:a copy -scodec mov_text {output_path}/subtitles_video.mp4'], shell=True,stdout=subprocess.PIPE, text=True)
