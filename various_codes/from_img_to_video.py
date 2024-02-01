import cv2
import os

# Directory containing your image files (change this to your image directory)
image_folder = r'C:\Users\17802\Dropbox\PC\Desktop\Tesis\Tesis 1\Codigos_prueba\Resorces\Images\video_de_natacion_original\Dataset1'

# Get a list of all image files in the directory
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
print(len(images))
frame = cv2.imread(os.path.join(image_folder, images[0]))
print(frame.shape[1], frame.shape[0])


def obtener_numero_de_nombre(nombre_archivo):
    # Suponemos que el formato es 'imgX.jpg'
    partes = nombre_archivo.split(".")[0].split("img")
    return int(partes[1])

# Ordenar la lista de archivos en función de los números extraídos
images = sorted(images, key=obtener_numero_de_nombre)


# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can also use other codecs like 'XVID'
video_name = r'C:\Users\17802\Dropbox\PC\Desktop\Tesis\Tesis 1\Codigos_prueba\Resorces\Videos\extras\output.mp4'  # Output video filename
output = cv2.VideoWriter(video_name, fourcc, 30, (1280, 720))         #664, 251

# Loop through the list of images and write them to the video
for image in images:
    img_path = cv2.imread(os.path.join(image_folder, image))
    img_path = cv2.resize(img_path, (1280, 720))         #664, 251
    print(os.path.join(image_folder, image))
    output.write(img_path)

# Release the VideoWriter
output.release()
print("Video created successfully!")
