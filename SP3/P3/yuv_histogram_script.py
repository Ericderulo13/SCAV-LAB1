#imports
from PIL import Image
import numpy as np
import subprocess
import  matplotlib.pyplot as plt
import numpy as np

class yuvi():
    def yuv_histogram(self,video,output):
        result = subprocess.run(["ffmpeg"], stdout=subprocess.PIPE, text=True)
        result1 = subprocess.run([f'ffmpeg -i {video} -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay" -c:a copy {output}/yuv_histogram.mp4'], shell=True,stdout=subprocess.PIPE, text=True)

