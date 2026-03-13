import os
import shutil

# 1. Configuración de carpetas y extensiones
EXTENSIONES = {
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Musica': ['.mp3', '.wav', '.flac'],
    'Instaladores': ['.exe', '.msi', '.zip', '.rar']
}

ruta_descargas = os.path.expanduser("~/Downloads")

def organizar():
    # 2. Revisar cada archivo en Descargas
    for archivo in os.listdir(ruta_descargas):
        ruta_original = os.path.join(ruta_descargas, archivo)
        
        # Saltamos si es una carpeta
        if os.path.isdir(ruta_original):
            continue
            
        # 3. Clasificar por extensión
        nombre, extension = os.path.splitext(archivo)
        extension = extension.lower()
        
        encontrado = False
        for carpeta, lista_ext en EXTENSIONES.items():
            if extension in lista_ext:
                ruta_destino = os.path.join(ruta_descargas, carpeta)
                
                # Crear carpeta si no existe
                if not os.path.exists(ruta_destino):
                    os.makedirs(ruta_destino)
                
                # Mover archivo
                shutil.move(ruta_original, os.path.join(ruta_destino, archivo))
                print(f"✅ Movido a {carpeta}: {archivo}")
                encontrado = True
                break
        
        if not encontrado and extension != "":
            print(f"❓ No sé qué hacer con: {archivo}")

if __name__ == "__main__":
    print("🚀 Iniciando súper organización...")
    organizar()
    print("✨ ¡Todo en su lugar!")