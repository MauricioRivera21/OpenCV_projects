import cv2
import os
import zipfile


## *************************************** Parametros a modificar: ******************************************
#video_name = "video_natacion_4.mp4"
video_name = "video_prueba14.mp4"
#video_name = r"Good_try\pre_swimmer_video_1.mp4"

comienzo_cuenta_frames = 0       #normalmente es 0 (depende del momento en que no hayan burbujas)
name_num_dataset = "Dataset"                   ## Dataset1, Dataset2, Dataset3...    NOTA!!!: se debe crear la carpeta antes de correr el codigo
## *********************************************************************************

####### 1) Extrayendo los frames del video #######
def extract_frames(video_path, output_path):
    # Abre el video
    video = cv2.VideoCapture(video_path)
    success, frame = video.read()
    count = 1486

    # Recorre los frames del video 2.5-4.5
    while success:
      if (count >= comienzo_cuenta_frames):
        # Guarda el frame actual como una imagen
        frame_path = f"{output_path}\img{count}.jpg"
        #print(frame_path)
        cv2.imwrite(frame_path, frame)
        count += 1

        # Lee el siguiente frame
        success, frame = video.read()
      else:
        # Lee el siguiente frame
        success, frame = video.read()
        count += 1

    # Cierra el video
    video.release()
    return count

# Ruta del video de entrada
video_path = r"C:\Users\17802\Dropbox\PC\Downloads"
#video_path = r"C:\Users\17802\Dropbox\PC\Desktop\Tesis\Tesis 1\Codigos_prueba\Face 3 - Evaluacion de nadador\video_swimmer\cell_phone_videos"
#video_path = r"C:\Users\17802\Dropbox\PC\Desktop\Tesis\Tesis 1\Codigos_prueba\Resorces\Videos"
video_path = os.path.join(video_path, video_name)
print("Input path: ", video_path)


# Ruta de salida para los frames
output_file_name = os.path.join(video_name[:-4], name_num_dataset)
#output_path = r"C:\Users\17802\Dropbox\PC\Desktop\Tesis\Tesis 1\Codigos_prueba\Resorces\Images"
#output_path = os.path.join(output_path, output_file_name)
output_path = r"C:\Users\17802\Dropbox\PC\Desktop\Tesis\Tesis 1\Codigos_prueba\Face 1 - Comparacion modelos\Yolov8\Yolo_trained\images\train"

print("Output path: ", output_path)

# Llama a la función para extraer los frames
count = extract_frames(video_path, output_path)
print(count)


"""
####### 2) Convirtiendo los frames a ZIP #######

# Directory containing the images (replace with your own directory path)
image_directory = '/content/frame_video_natacion/'

# List all image files in the directory
image_files = [f for f in os.listdir(image_directory) if os.path.isfile(os.path.join(image_directory, f))]

# Create a zip file
zip_path = '/content/frame_video_natacion.zip'
with zipfile.ZipFile(zip_path, 'w') as zip_file:
    for file in image_files:
        # Add each image file to the zip
        zip_file.write(os.path.join(image_directory, file), arcname=file)

# Download the zip file
from google.colab import files
files.download(zip_path)
"""