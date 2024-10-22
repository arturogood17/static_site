import os
import shutil

def copypath(origen, destino):
    if not os.path.exists(destino):
       os.mkdir(destino)

    for filename in os.listdir(origen): #recorres la lista de archivos en origen
        from_path= os.path.join(origen, filename) #guardas origen para ver qué pasa
        dest_path = os.path.join(destino, filename) #guardas destino para ver qué pasa
        print(f"* {from_path} ---> {dest_path}")
        if os.path.isfile(from_path): #revisas que es un archivo
            shutil.copy(from_path, dest_path) #si lo es, lo copias
        else:
            copypath(from_path, dest_path) #si no, lo recorres y haces el proceso, pero empezando desde los últimos paths