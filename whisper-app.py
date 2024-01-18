import streamlit as st
import speech_recognition as sr

st.title("Multi-lingual Transcription using SpeechRecognition")

audio_file = st.file_uploader("Upload your audio", type=["wav", "mp3", "m4a"])

if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing...")
        recognizer = sr.Recognizer()

        with audio_file as source:
            audio_data = recognizer.record(source)

        try:
            transcription = recognizer.recognize_google(audio_data)
            st.sidebar.success("Transcription complete")
            st.markdown(transcription)

        except sr.UnknownValueError:
            st.sidebar.error("Could not understand audio")
        except sr.RequestError as e:
            st.sidebar.error(f"Error connecting to Google Web Speech API: {e}")

    else:
        st.sidebar.error("Please upload an audio file.")
