from PIL import Image
import numpy as np
import subprocess
import  matplotlib.pyplot as plt
import numpy as np

class subtitles():
    # Exercice 4
    def subtitles_performing(self,video, subtitles):
        result = subprocess.run(["ffmpeg"], stdout=subprocess.PIPE, text=True)
        result = subprocess.run(
            [f'ffmpeg -i {video} -vf "subtitles=eric.srt" -c:a copy -scodec mov_text subtitles_video.mp4'], shell=True,stdout=subprocess.PIPE, text=True)
