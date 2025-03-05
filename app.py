import streamlit as st
from pydub import AudioSegment
import os

# Título de la aplicación con logo
col1, col2 = st.columns([1, 6])
with col1:
    st.image("logo.jpg", width=100, use_container_width=True)
with col2:
    st.title("Analizador de Velocidad Lectora")

print(AudioSegment.converter)
# Configurar la ruta de FFmpeg (si no se detecta automáticamente)
AudioSegment.converter = "C:\\ffmpeg\\bin\\ffmpeg.exe"

# Subida de archivo de audio
audio_subido = st.file_uploader("Sube tu grabación", type=["wav", "mp3", "m4a", "ogg", "aac"])

# Campo para pegar el texto de referencia
texto_referencia = st.text_area("Pega el texto a leer")

# Mostrar el texto y el archivo subido (para depuración)
if texto_referencia:
    st.write("Texto de referencia:")
    st.write(texto_referencia)

if audio_subido:
    st.write("Archivo de audio subido:")
    st.audio(audio_subido)

 # Convertir el audio a WAV si no está en ese formato
    if audio_subido.name.endswith(".wav"):
        st.write("El archivo ya está en formato WAV.")
        audio_wav = audio_subido
    else:
        st.write("Convirtiendo el archivo a WAV...")
        try:
            # Guardar el archivo subido temporalmente
            with open("temp_audio", "wb") as f:
                f.write(audio_subido.getbuffer())

            # Cargar el archivo con pydub
            audio = AudioSegment.from_file("temp_audio")

            # Convertir a WAV
            audio_wav_path = "temp_audio.wav"
            audio.export(audio_wav_path, format="wav")

            # Mostrar el archivo convertido
            st.write("Archivo convertido a WAV:")
            st.audio(audio_wav_path)

            # Eliminar el archivo temporal
            os.remove("temp_audio")
        except Exception as e:
            st.error(f"Error al convertir el archivo: {e}")


