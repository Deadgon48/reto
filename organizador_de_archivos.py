# organizador_de_archivos.py

import os
import shutil

carpeta_origen = "archivos"
carpeta_destino = "organizados"

if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

for archivo in os.listdir(carpeta_origen):
    ruta = os.path.join(carpeta_origen, archivo)

    if archivo.endswith(".txt"):
        destino = os.path.join(carpeta_destino, "textos")
    elif archivo.endswith(".jpg"):
        destino = os.path.join(carpeta_destino, "imagenes")
    else:
        destino = os.path.join(carpeta_destino, "otros")

    if not os.path.exists(destino):
        os.makedirs(destino)

    shutil.move(ruta, destino)

print("Archivos organizados correctamente")