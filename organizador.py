import os
import shutil

# 1. Definimos la ruta de Descargas (ajusta 'TuUsuario')
# En Windows suele ser: C:/Users/TuUsuario/Downloads
ruta_descargas = os.path.expanduser("~/Downloads")
ruta_destino = os.path.join(ruta_descargas, "Documentos_PDF")

# 2. Creamos la carpeta de destino si no existe
if not os.path.exists(ruta_destino):
    os.makedirs(ruta_destino)
    print(f"Carpeta creada en: {ruta_destino}")

# 3. Listamos los archivos y movemos los PDFs
for archivo in os.listdir(ruta_descargas):
    if archivo.endswith(".pdf"):
        ruta_original = os.path.join(ruta_descargas, archivo)
        shutil.move(ruta_original, ruta_destino)
        print(f"Movido: {archivo}")

print("¡Limpieza terminada!")