import cv2
import os

# Directory containing your image files (change this to your image directory)
video_name = "vid7"
image_folder = r'C:\Users\17802\Dropbox\PC\Desktop\Tesis\Tesis 1\Codigos_prueba\Resorces\Images'
image_folder = os.path.join(image_folder, video_name, "Dataset")

# Get a list of all image files in the directory
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
print(len(images))
frame = cv2.imread(os.path.join(image_folder, images[0]))

for img_name in images:
    img_path = os.path.join(image_folder, img_name)
    img = cv2.imread(img_path)

    if img is not None:
        img_flipped = cv2.flip(img, 1)  # Aplica el flip horizontal

        # Obten el nombre del archivo sin la extensión
        name, ext = os.path.splitext(img_name)

        # Crea un nuevo nombre de archivo con "_flipped" y la misma extensión
        new_img_name = f"{name}_flipped{ext}"

        # Guarda la imagen con el nuevo nombre
        #new_img_path = os.path.join(image_folder, new_img_name)
        new_img_path = os.path.join(image_folder, img_name)
        cv2.imwrite(new_img_path, img_flipped)