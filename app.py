import streamlit as st
import librosa
import soundfile as sf
import noisereduce as nr
import numpy as np
import io

st.title("Audio Noise Reduction Tool")

uploaded = st.file_uploader("upload an audio file (wav, mp3)", type=["wav", "mp3"])

if uploaded:
    y, sr = librosa.load(uploaded, sr=None, mono=True)
    reduce = nr.reduce_noise(y=y, sr=sr)

    buf_orig = io.BytesIO()
    sf.write(buf_orig, y, sr, format="WAV")
    buf_clean = io.BytesIO()
    sf.write(buf_clean, reduce, sr, format="WAV")

    st.subheader("Original Audio")
    buf_orig.seek(0)
    st.audio(buf_orig)

    st.subheader("Cleaned Audio")
    buf_clean.seek(0)
    st.audio(buf_clean)

    buf_clean.seek(0)
    st.download_button("Download cleaned Audio", buf_clean, file_name="cleaned.wav", mime="audio/wav")