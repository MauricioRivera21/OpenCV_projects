import os
import shutil

# Ruta del directorio que contiene los archivos:
video_name = "vid5"
directorio = r'C:\Users\17802\Dropbox\PC\Desktop\Tesis\Tesis 1\Codigos_prueba\Resorces\Images'
directorio = os.path.join(directorio, video_name, "Dataset")

# Obtener una lista de archivos .jpg en el directorio
archivos_jpg = [archivo for archivo in os.listdir(directorio) if archivo.endswith(".jpg")]      #para archivos jpg
#archivos_jpg = [archivo for archivo in os.listdir(directorio) if archivo.endswith(".txt")]      #para archivos txt
count = 0

# Función personalizada para extraer el número de cada nombre de archivo
def obtener_numero_de_nombre(nombre_archivo):
    partes = nombre_archivo.split(".")[0].split("img")      # Suponemos que el formato es 'imgXX.jpg'
    return int(partes[1])

# Ordenar la lista de archivos en función de los números extraídos
archivos_jpg_ordenados = sorted(archivos_jpg, key=obtener_numero_de_nombre)
#print(archivos_jpg_ordenados)


# Iterar a través de los archivos y cambiarles el nombre
for i, nombre_archivo in enumerate(archivos_jpg_ordenados):
    #nuevo_nombre = f"img{count}.jpg"
    _ = obtener_numero_de_nombre(nombre_archivo)

    #nuevo_nombre = f"predicted_Keypoints{count}.txt" 
    nuevo_nombre = f"img{count}.jpg" 
    ruta_original = os.path.join(directorio, nombre_archivo)
    ruta_nuevo = os.path.join(directorio, nuevo_nombre)
    
    ## Renombrar el archivo
    try:
        shutil.move(ruta_original, ruta_nuevo)
        print(f"Renombrado: {nombre_archivo} -> {nuevo_nombre}")
        count = count + 1
    except Exception as e:
        print(f"Error al renombrar {nombre_archivo}: {str(e)}")
