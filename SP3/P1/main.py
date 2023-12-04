#imports
from PIL import Image
import numpy as np
import subprocess
import  matplotlib.pyplot as plt
#Exercici1
def rgb_yuv_convertor(val1, val2, val3, a):
  if (a =="rgb"):#from rgb to yuv
    R = 1.164 *(val1-16) + 1.596 * (val3 -128)
    G = 1.164 *(val1-16) - 0.813* (val3 -128) -0.391*(val2-128)
    B = 1.164 *(val1-16) + 2.018 *(val2-128)
    return (R,G,B)
  if(a=="yuv"):
    Y = 0.257 * val1 + 0.504*val2 +0.098*val3 +16
    U = -0.148*val1 -0.291*val2 +0.439 * val3 +128
    V = 0.439 * val1 -0.368*val2 -0.071 * val3 +128
    return (Y,U,V)


  return ("Put rgb or yuv type in order to do the convertion")

def resize(image,width,height):
    result = subprocess.run(["ffmpeg"], stdout=subprocess.PIPE , text =True)
    result2 = subprocess.run([f'ffmpeg -i {image} -vf "scale={width}:{height}" resizedimage.jpg '],shell=True, stdout=subprocess.PIPE, text=True)
#Exercici 3
def zigzag_compress(matrix):

    rows, cols = len(matrix), len(matrix[0])
    compressed = []
    row, col = 0, 0
    going_up = True

    for _ in range(rows * cols):
        compressed.append(matrix[row][col])

        if going_up:
            if row > 0 and col < cols - 1:
                row -= 1
                col += 1
            elif col == cols - 1:
                row += 1
                going_up = False
            elif row == 0:
                col += 1
                going_up = False
        else:
            if row < rows - 1 and col > 0:
                row += 1
                col -= 1
            elif row == rows - 1:
                col += 1
                going_up = True
            elif col == 0:
                row += 1
                going_up = True

    return compressed
# Exercici 4

def black_white(image):
    result = subprocess.run(["ffmpeg"], stdout=subprocess.PIPE , text =True)
    result2 = subprocess.run([f'ffmpeg -i {image} -vf format=gray black_white.jpg'],shell=True, stdout=subprocess.PIPE, text=True)
    result2 = subprocess.run([f'ffmpeg -i black_white.jpg -q:v 31 black_white_compressed.jpg '], shell=True,stdout=subprocess.PIPE, text=True)
    return "black_white_compressed.jpg"
#Exercici 5

def run_length_encoding(numeros):
    lista = []
    contador = 1

    for i in range(1, len(numeros)):
        if numeros[i] == numeros[i - 1]:
            contador += 1
        else:
            if contador == 0:
                if numeros[i - 1] == 0:
                    lista.append((numeros[i - 1]))
                    lista.append(contador+1)
                else:
                    lista.append(numeros[i - 1])
            else:
                if numeros[i - 1] == 0:
                    lista.append((numeros[i - 1], contador+1))
                else:
                    for j in range (contador):
                        lista.append(numeros[i - 1])
                    contador=0
            contador=0
    if numeros[-1]==0:
        lista.append((numeros[- 1], contador + 1))
    else:
        lista.append(numeros[-1])

    return lista



#EXERCICI 6

import cv2
import numpy as np
# Load the image
#encoder
class dct:
    def dctencoder(imagen):
        image = cv2.imread(imagen)
        # Convert to YUV color space
        yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
        # Split the YUV image into Y, U, and V components
        y, u, v = cv2.split(yuv_image)
        y_float = y.astype(np.float32)
        u_float = u.astype(np.float32)
        v_float = v.astype(np.float32)

        dct_y = cv2.dct(y_float)
        dct_u = cv2.dct(u_float)
        dct_v = cv2.dct(v_float)

        yuv_image = cv2.merge((dct_y,dct_u,dct_v))
        bgr_image = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR)
        fig1,ax1=plt.subplots()
        ax1.imshow(bgr_image)
        plt.savefig("1dctimage")
        return bgr_image
    def dctdecoder(imagen):
        yuv_image = cv2.cvtColor(imagen, cv2.COLOR_BGR2YUV)
        # Split the YUV image into Y, U, and V components
        y, u, v = cv2.split(yuv_image)
        y_float = y.astype(np.float32)
        u_float = u.astype(np.float32)
        v_float = v.astype(np.float32)

        dct_y = cv2.idct(y_float)
        dct_u = cv2.idct(u_float)
        dct_v = cv2.idct(v_float)
        yuv_image = cv2.merge((dct_y,dct_u,v_float))
        decoded_image = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR)
        fig2,ax2=plt.subplots()
        ax2.imshow(decoded_image)
        plt.savefig("recoveredimage")
        return decoded_image


#Exercicis exceutables
if __name__ == "__main__":
    print(rgb_yuv_convertor(16.33,127.854,127.9406,"rgb"))
    resize("bbb.mp4",400,400)#Resized Image

    image = Image.open("resizedimage.jpg")
    #Transforming the image to a matrix a form,
    matrix2= np.array(image)
    width=matrix2.shape[0]
    height= matrix2.shape[1]
    compressed_data = zigzag_compress(matrix2)
    #Transforming the resulting list from zigzag_compress and plotting the resultant image.
    compressed_data=np.array(compressed_data)
    imagen = Image.fromarray(compressed_data.reshape(width,height,3).astype('uint8'))
    fig,ax=plt.subplots()
    ax.imshow(imagen, cmap='viridis')
    plt.savefig("serpentine2") #Serpentine method.


    #run length encoding
    lista=[]
    lista_bytes = 14,14,0,0,0,0,4,0,3,0,0,1
    lista=run_length_encoding(lista_bytes)

    flattened_list = []
    for item in lista:
        if isinstance(item, tuple):
            flattened_list.extend(item)
        else:
            flattened_list.append(item)

    print(flattened_list) # encode list

    black_white("resizedimage.jpg") # black_white and compressed
    #Exercici 6
    encoded_image=dct.dctencoder("msn.jpg")
    decoded_image = dct.dctdecoder(encoded_image)
