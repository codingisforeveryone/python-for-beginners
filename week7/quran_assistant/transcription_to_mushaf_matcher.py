

class TranscriptionToMushafMatcher:

    def __init__(self, mushaf_file, translation_file, uthmani_file):
        
        self.mushaf = []
        self.translation = []
        self.mushaf_uthmani = []
        self.index = None # this is the line of the text files to find

        mushaf_surah = []
        mushaf_aya = []
        translation_surah = []
        translation_aya = []
        uthmani_surah = []
        uthmani_aya = []
        with open(mushaf_file, "r", encoding="utf-8") as file:
            for line in file:
                surah_ayah_text = line.split("|", 2)
                if len(surah_ayah_text) < 3:
                    break
                mushaf_surah.append(surah_ayah_text[0])
                mushaf_aya.append(surah_ayah_text[1])
                self.mushaf.append(surah_ayah_text[2])

        with open(translation_file, "r") as file:
            for line in file:
                surah_ayah_text = line.split("|", 2)
                if len(surah_ayah_text) < 3:
                    break
                translation_surah.append(surah_ayah_text[0])
                translation_aya.append(surah_ayah_text[1])
                self.translation.append(surah_ayah_text[2])

        with open(uthmani_file, "r", encoding="utf-8") as file:
            for line in file:
                surah_ayah_text = line.split("|", 2)
                if len(surah_ayah_text) < 3:
                    break
                uthmani_surah.append(surah_ayah_text[0])
                uthmani_aya.append(surah_ayah_text[1])
                self.mushaf_uthmani.append(surah_ayah_text[2])
            
        assert translation_surah == mushaf_surah
        assert translation_aya == mushaf_aya
        assert uthmani_aya == mushaf_aya
        assert uthmani_surah == mushaf_surah

    def find_ayah(self, text):
        for index, line in enumerate(self.mushaf):
            if text.strip() in line.strip():
                self.index = index
                break
    
    def get_current_translation(self):
        return self.translation[self.index]

    def get_current_mushaf_uthmani(self):
        return self.mushaf_uthmani[self.index]


