import os
import shutil

# --- Configuración ---
ruta_input = input("Introduce la ruta de la carpeta a ordenar: ").strip()
carpeta_a_ordenar = os.path.normpath(ruta_input)

# Diccionario con carpetas destino por tipo de archivo
tipos_de_archivo = {
    "videos": [".mp4", ".avi", ".mkv", ".mov", ".flv", ".wmv"],
    "audios": [".mp3", ".wav", ".aac", ".ogg", ".flac", ".m4a"],
    "pdf": [".pdf"],
    "excel": [".xls", ".xlsx", ".ods", ".xlsm", ".csv"],  # si prefieres, deja .csv en su carpeta propia
    "word": [".doc", ".docx", ".rtf", ".txt", ".TXT"],    # incluye .txt como pediste
    "imagenes": [
        ".jpeg", ".jpg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp",
        ".heic", ".heif", ".ico", ".svg", ".eps", ".ai", ".raw", ".psd", ".xcf"
    ],
    "python": [".py"],
    "csv": [".csv"],             # si quieres separar CSV, deja esta línea y quita ".csv" de "excel"
    # "css": [".css"],           # estaba en tu CSV por error; si quieres, crea su propia carpeta
}

# Si quieres mandar lo no clasificado a "otros", pon True
enviar_no_clasificados_a_otros = True
nombre_carpeta_otros = "otros"

def crear_carpeta_si_no_existe(carpeta):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

def mover_archivo_or_guardar_unico(origen, carpeta_destino):
    """
    Mueve el archivo 'origen' a 'carpeta_destino'.
    Si existe un archivo con el mismo nombre, añade un sufijo (1), (2), ...
    """
    crear_carpeta_si_no_existe(carpeta_destino)
    base = os.path.basename(origen)
    nombre, ext = os.path.splitext(base)
    destino = os.path.join(carpeta_destino, base)

    if not os.path.exists(destino):
        shutil.move(origen, destino)
        return

    # Buscar un nombre disponible con sufijo
    i = 1
    while True:
        candidato = os.path.join(carpeta_destino, f"{nombre} ({i}){ext}")
        if not os.path.exists(candidato):
            shutil.move(origen, candidato)
            return
        i += 1

def clasificar_archivo(ruta_archivo):
    extension = os.path.splitext(ruta_archivo)[1].lower()
    for carpeta_destino, extensiones in tipos_de_archivo.items():
        if extension in extensiones:
            return carpeta_destino
    return None

# --- Proceso ---
if not os.path.isdir(carpeta_a_ordenar):
    raise SystemExit("La ruta indicada no es una carpeta válida.")

for nombre in os.listdir(carpeta_a_ordenar):
    ruta_completa = os.path.join(carpeta_a_ordenar, nombre)

    # Ignora directorios y accesos directos a carpetas
    if not os.path.isfile(ruta_completa):
        continue

    carpeta_categoria = clasificar_archivo(ruta_completa)

    if carpeta_categoria is None:
        if enviar_no_clasificados_a_otros:
            destino_final = os.path.join(carpeta_a_ordenar, nombre_carpeta_otros)
            mover_archivo_or_guardar_unico(ruta_completa, destino_final)
        # Si no quieres mover no clasificados, simplemente continue
        continue

    destino_final = os.path.join(carpeta_a_ordenar, carpeta_categoria)
    mover_archivo_or_guardar_unico(ruta_completa, destino_final)

print("Ordenación completada.")
