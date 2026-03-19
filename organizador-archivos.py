# organizador-archivos.py
# **Autor:** Humberto
# **Fecha:** 18/03/2026
# **Contenido:** Script en Python para clasificar archivos (.txt, .jpg)
# desde una carpeta de origen a carpetas organizadas por tipo.

import os
import shutil

carpeta_origen = "archivos"
carpeta_destino = "organizados"

# Asegurar que la carpeta destino existe
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

def organizar():
    for archivo in os.listdir(carpeta_origen):
        ruta = os.path.join(carpeta_origen, archivo)

        # Saltarse si es un directorio
        if os.path.isdir(ruta):
            continue

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

if __name__ == "__main__":
    organizar()