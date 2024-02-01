import os


# Función personalizada para extraer el número de cada nombre de archivo
def obtener_numero_de_nombre(nombre_archivo):
    partes = nombre_archivo.split(".")[0].split("img")
    return int(partes[1])

# Ruta del directorio que contiene los archivos:
directorio = r'C:\Users\17802\Dropbox\PC\Desktop\Tesis\Tesis 1\Codigos_prueba\Face 1 - Comparacion modelos\Yolov8\Yolo_trained\labels\train'

# Obtener una lista de archivos .jpg en el directorio
archivos_jpg = [archivo for archivo in os.listdir(directorio) if archivo.endswith(".txt")]
count = 0


# Ordenar la lista de archivos en función de los números extraídos
archivos_jpg_ordenados = sorted(archivos_jpg, key=obtener_numero_de_nombre)
#print(archivos_jpg_ordenados)


# Iterar a través de los archivos y cambiarles el nombre
for i, nombre_archivo in enumerate(archivos_jpg_ordenados):
    #nuevo_nombre = f"img{count}.jpg"
    partes = obtener_numero_de_nombre(nombre_archivo)
    if (partes != count):
        print(count)
        break
    
    count = count + 1
