


class AudioRecorder:
    def __init__(self, save_folder):
        self.save_folder = save_folder
        self.current_file = "002005.mp3"

    def get_current_file(self):
        return self.current_file

    def save_mp3_from_audio(self):
        raise NotImplementedError()

    def delete_old_mp3s(self):
        raise NotImplementedError()