# Organizador-Archivos
Organiza los archivos segun su clase y los guarda en carpetas clasificadoras
# Organizador de Archivos 🗂️

Pequeño script en **Python** que **ordena los archivos de una carpeta por tipo** moviéndolos a subcarpetas (vídeos, imágenes, pdf, excel, word, etc.).  
Está pensado para limpiar carpetas como *Descargas* en un clic.

> ⚠️ Nota: el script **mueve** los archivos (no los copia) y **no toca carpetas**.  
> Si en destino ya existe un archivo con el mismo nombre, se crea uno con sufijo: `nombre (1).ext`, `nombre (2).ext`, etc.

---

## 🚀 Requisitos

- Python **3.8+**
- Sistema operativo Windows, macOS o Linux

---

## 📦 Instalación

Clona el repositorio y entra en la carpeta:

```bash
git clone https://github.com/Javierfiestasbotella/Organizador-Archivos.git
cd Organizador-Archivos
(Instalar un entorno virtual es opcional.)

▶️ Uso
Ejecuta el script principal (ajusta el nombre si tu archivo se llama distinto, por ejemplo organizador.py):

bash
Copiar
Editar
python organizador.py
El programa te pedirá la ruta de la carpeta a ordenar, por ejemplo:

Windows: C:\Users\TuUsuario\Downloads

macOS/Linux: /Users/tuusuario/Downloads o /home/tuusuario/Descargas

Pulsa Enter y el script clasificará los archivos.

🧩 Categorías por defecto
Estas son las carpetas y extensiones configuradas (puedes modificarlas en el diccionario tipos_de_archivo):

videos: .mp4, .avi, .mkv, .mov, .flv, .wmv

audios: .mp3, .wav, .aac, .ogg, .flac, .m4a

pdf: .pdf

excel: .xls, .xlsx, .ods, .xlsm (opcionalmente .csv)

word: .doc, .docx, .rtf, .txt

imagenes: .jpeg, .jpg, .png, .gif, .bmp, .tiff, .tif, .webp, .heic, .heif, .ico, .svg, .eps, .ai, .raw, .psd, .xcf

python: .py

csv: .csv (si prefieres separarlos de Excel)

Además, el script puede mandar lo no reconocido a la carpeta otros si está activada la opción.

🛠️ Personalización
Añadir/editar categorías: modifica el diccionario tipos_de_archivo en el código.

Enviar no clasificados a otros: ajusta la variable enviar_no_clasificados_a_otros = True/False.

Conflictos de nombre: ya viene resuelto con el sistema de sufijos (1), (2), …

No se crean subcarpetas innecesarias: solo se crean cuando realmente hay algo que mover.

💡 Ejemplo rápido
Entrada:

Copiar
Editar
/Descargas
  ├── foto.jpg
  ├── Informe.docx
  ├── Pelicula.mkv
  ├── notas.txt
  └── desconocido.xyz
Salida:

bash
Copiar
Editar
/Descargas
  ├── imagenes/foto.jpg
  ├── word/Informe.docx
  ├── videos/Pelicula.mkv
  ├── word/notas.txt
  └── otros/desconocido.xyz   (si está activado)
❓ Preguntas frecuentes
¿Qué pasa si ya existen las carpetas?
Nada, el script las usa. Solo crea las que falten.

¿Por qué no veo cambios?
Asegúrate de haber introducido bien la ruta y de que haya archivos (no carpetas) en ella.

¿Puedo revertirlo?
El script mueve archivos. Si quieres deshacer, tendrás que volver a colocarlos manualmente o con otro script.

🤝 Contribuir
¡Se aceptan mejoras! Haz un fork, crea una rama y abre un Pull Request:

bash
Copiar
Editar
git checkout -b feat/mi-mejora
git commit -m "Añade X"
git push origin feat/mi-mejora
