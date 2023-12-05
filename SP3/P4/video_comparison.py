
from PIL import Image
import numpy as np
import subprocess
import  matplotlib.pyplot as plt
import numpy as np

class comp():
# Exercici 2
    def video_comparison(self, video1, video2, output_path):
        result = subprocess.run(["ffmpeg"], stdout=subprocess.PIPE, text=True)
        result1 = subprocess.run([
                                     f'ffmpeg -i {video1} -i {video2} -filter_complex "[0:v]scale=iw/2:ih/2 [left]; [1:v]scale=iw/2:ih/2 [right]; [left][right]hstack" {output_path}/comparison_video.mp4'],
                                 shell=True, stdout=subprocess.PIPE, text=True)
        return "comparison_video.mp4"
