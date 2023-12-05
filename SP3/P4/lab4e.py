import os

from PIL import Image
import numpy as np
import subprocess
import docker
import getpass
import  matplotlib.pyplot as plt
import numpy as np
import PySimpleGUI as sg
import P2.LAB2 as p2
import P4.video_comparison as compare
import P3.yuv_histogram_script as py
import P3.subtiles_script as ps
import time
import io
import base64
from PIL import Image, ImageSequence
from PIL import Image, ImageTk
import threading
class lab4():

    #Ecxercici1
    def vp8_vp9_h265_av1(self,video):
        res1= p2.lab2().resolution_modifying(video) #720
        res2 =p2.lab2().resolution_modifying(video) #480
        result = subprocess.run(["ffmpeg"], stdout=subprocess.PIPE, text=True)
        result1 = subprocess.run([f'ffmpeg -i new_bbb_resolution_{res1}.mp4 -c:v libvpx -b:v 1M -c:a libvorbis vp8_{res1}p_video.webm'], shell=True,stdout=subprocess.PIPE, text=True)
        result2 =subprocess.run([f'ffmpeg -i new_bbb_resolution_{res2}.mp4 -c:v libvpx-vp9 -b:v 2M -c:a libopus vp9_{res2}p_video.webm'], shell=True,stdout=subprocess.PIPE, text=True)
        result3 =subprocess.run([f'ffmpeg -i new_bbb_resolution_{res1}.mp4 -c:v libx265 -crf 20 -preset medium -c:a aac -b:a 128k h265_{res1}p.mp4'], shell=True,stdout=subprocess.PIPE, text=True)
        #result4 =subprocess.run([f'ffmpeg -i new_bbb_resolution_720.mp4 -c:v libaom-av1 -crf 20 -b:v 0 -strict experimental -cpu-used 0 -c:a libopus -b:a 128k av1_480p.mkv'], shell=True,stdout=subprocess.PIPE, text=True)# funciona pero va massa lent

    def convert_file_to_base64(self,filename):
        try:
            contents = open(filename, 'rb').read()
            encoded = base64.b64encode(contents)
            sg.clipboard_set(encoded)
            # pyperclip.copy(str(encoded))
            sg.popup('Copied to your clipboard!', 'Keep window open until you have pasted the base64 bytestring')
        except Exception as error:
            sg.popup_error('Cancelled - An error occurred', error)
    # Exercici 3 GUI
    def gui_interface(self):

        layout = [
            [sg.Text("First video"), sg.Input(key="-IN-"), sg.FileBrowse()],
            [sg.Text("Second video"), sg.Input(key="-IN2-"), sg.FileBrowse()],
            [sg.Text("Output Video"), sg.Input(key="-OUT-"), sg.FolderBrowse()],
            [sg.Text("Select video to modify resolution/add subtitle/showing YUV:"),sg.Radio("First video", "RADIO1", default=True, key="-VIDEO-"),sg.Radio("Second video", "RADIO1", key="-VIDEO2-")],
            [sg.Exit(),sg.Button("Video Comparison"),sg.Button("Subtitles Performing"), sg.Button("YUV"),sg.Button("",image_data=b'iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAMAAAC6V+0/AAABgFBMVEX////tuwAATZjbADClAEQAAAD/7QLxvgD/8AD/+QDxqRbYADLmbiT/9QCnAEIAUJ33wwBTQSGOHVj3yhCUAD9ZQQ59JGSrAD4zQYhWNHkAQYu8vcHZABn30df1wMmqACbbACPeGyyMagDfLSzrkZ3cIDfktACXjwCEZACGcQBFOoCGH17w8PCZmgDAmACiACbAvAAnHwAUFBQ6LgDKoADXqgDd3d2AgIBpaWmxjACjo6MQDQCigABvWABaRwCVlZVAQEAZFABENgBDCh7Ly8uVdgBXV1cnJycyMjIvJQC4gRGxTBxOPgAAM3MAJmcAGDQ4AB1UABVqAB1vTg5CHBBiVgBXEhJQSQA6IQxIKQq9ACpsaQC5HzzDKSd8AB91YB5OSDphNUZgW0xeVDtcUCrm2ACtpgBWKQ59ewBOVWPmdYW6nKhZIRJeNwxrAAiiABWhgo+wa3oAGExzADNZACNhDlUAAUgFGkMdIi9BOCAsIxgAABcyAD1FHFsxFw0oCw94qDTEAAAAyElEQVR4nHXRTQrCMBAF4L7GMQoKXSioSxdZScGfWqsVRTQIdusJRLyB5zd5EemiPkgYPpJOmkRRc+YiAoi1fhbZEWEfa6W2xtxU5/m6gyhuKBVF7Z7qdFV/TtwUiglYHIkzU0dzDiun9e3ltemb3+4+KTLolKW3jJU7IxJhaRxWCKl0smSxd7iYxqNWK47DGMdD3+NQBNSYEC+WjYgaKInhNw0Re1TEhGjh8Z3i5BGHcHeCwa8R5Hel7oDZamVQIyYH8j+vEPIByJQRbhFVVrgAAAAASUVORK5CYII=',key="?",size=(10,10))],
        ]
        window = sg.Window("SCAV GUI", layout, size=(700, 400), grab_anywhere=True, finalize=True,transparent_color=sg.theme_background_color("Dark green"))
        while True:
            event, values = window.read()
            print(event, values)
            if event in (sg.WINDOW_CLOSED, "Exit"):
                break
            if event == "Video Comparison":
                compare.comp().video_comparison(values["-IN-"],values["-IN2-"],values["-OUT-"])
                print("Video comparison done. See it in your output folder")
            if event == "YUV":
                if values["-VIDEO-"]:
                    py.yuvi.yuv_histogram(self, values["-IN-"],values["-OUT-"])
                    print("YUV done", values["-IN-"])
                elif values["-VIDEO2-"]:
                    py.yuvi.yuv_histogram(self,values["-IN2-"],values["-OUT-"])
                    print("YUV DONE", values["-IN2-"])
            if event == "Subtitles Performing":
                files = sg.popup_get_file('Seleccione los subtítulos que quiera añadir:',file_types=(("Archivos SRT", "*.srt"),))
                if values["-VIDEO-"]:
                    ps.subtitles.subtitles_performing(self,values["-IN-"],files,values["-OUT-"])
                    print("Subtitles added in", values["-OUT-"])
                elif values["-VIDEO2-"]:
                    ps.subtitles.subtitles_performing(self,values["-IN2-"],files,values["-OUT-"])
                    print("Subtiles added in",values["-OUT-"])

            if event == "?":
                gif_filename = r'msn.gif'

                layout = [[sg.Text('Javi Bon nadal!!', background_color='#A37A3B', text_color='#FFF000',
                                   justification='c', key='-T-', font=("Wide Latin", 40))],
                          [sg.Image(key='-IMAGE-')]]
                window1= sg.Window('Window Title', layout, element_justification='c', margins=(0, 0),
                                   element_padding=(0, 0), finalize=True)

                window1['-T-'].expand(True, True, True)  # Make the Text element expand to take up all available space

                interframe_duration = Image.open(gif_filename).info['duration']  # get how long to delay between frames

                while True:
                    for frame in ImageSequence.Iterator(Image.open(gif_filename)):
                        event, values = window1.read(timeout=interframe_duration)
                        if event == sg.WIN_CLOSED:  # Check if the window is closed
                            break
                        window1['-IMAGE-'].update(data=ImageTk.PhotoImage(frame))
                    if event == sg.WIN_CLOSED:
                        window1.close()# Check if the window is closed
                        break

        window.close()


    # Exercici 4
    #play a bit
    def bit_docker(self,name,container):
        # Command to build the Docker image
        import subprocess
        import time

        # Comandos de Docker que se desean ejecutar
        docker_commands = [
            f"sudo -S docker build -t {name}:latest /home/eric/PycharmProjects/SCAVPROJECT/P4",
            f"sudo -S docker run -d --name {container} {name}"
        ]

        # Combinar los comandos de Docker en uno solo para la creación del contenedor
        combined_command = " && ".join(docker_commands)

        # Ejecutar los comandos para crear el contenedor
        subprocess.run(combined_command, shell=True)

        # Esperar unos segundos para asegurarse de que el contenedor esté en ejecución
        time.sleep(6)
        # Comando para copiar archivos del contenedor al directorio local
        copy_command = f"sudo -S docker cp {container}:/app /home/eric/PycharmProjects/SCAVPROJECT/P4"
        # Ejecutar el comando para copiar archivos
        subprocess.run(copy_command, shell=True)

    # Exercici
if __name__ == "__main__":
    l4 = lab4()
    result = subprocess.run(["ffmpeg"], stdout=subprocess.PIPE, text=True)
    result1 = subprocess.run([f'ffmpeg -i bbb.mp4 -ss 00:03:00 -t 00:00:05 -c:v copy -c:a copy bbb5.mp4'], shell=True,stdout=subprocess.PIPE, text=True)
    #l4.vp8_vp9_h265_av1("bbb5.mp4") #funciona
    l4.bit_docker("tt13","tt14")
    #l4.gui_interface()  # Video comparison inside(funciona)
