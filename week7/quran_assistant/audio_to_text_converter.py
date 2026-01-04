import whisper
import os

class AudioToTextConverter:

    def __init__(self, save_folder):
        self.save_folder = save_folder
        self.model = whisper.load_model("small")

    def convert_audio_to_text(self, file_name):
        file = os.path.join(self.save_folder, file_name)
        result = self.model.transcribe(file, language="ar")
        return result["text"]
    