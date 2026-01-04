from transcription_to_mushaf_matcher import TranscriptionToMushafMatcher
from audio_to_text_converter import AudioToTextConverter
from audio_recorder import AudioRecorder
from visualizer import visualize_ayah_and_translation
import streamlit as st

st.title("📖 Quran Audio-Text Assistant")



if st.button("Start Recording (for now: just start programm)"):
    
    audio_recorder = AudioRecorder("data")
    current_file = audio_recorder.get_current_file()
    
    audio_to_text = AudioToTextConverter("data")
    text = audio_to_text.convert_audio_to_text(current_file)

    #text = ' أولئك على هدى من ربهم وأولئك هم المفلحون'
    matcher = TranscriptionToMushafMatcher("quran-simple-clean.txt", "en.sahih.txt", "quran-uthmani.txt")
    matcher.find_ayah(text)

    #current_ayah = matcher.get_current_ayah()
    current_translation = matcher.get_current_translation()
    current_mushaf_uthmani = matcher.get_current_mushaf_uthmani()
    visualize_ayah_and_translation(current_mushaf_uthmani, current_translation)





