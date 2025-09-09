from pydub.silence import split_on_silence
# from src.utils.logger import Logger
import speech_recognition as sr
from pydub import AudioSegment
import shutil
import os


# logger setup
# logger = Logger.get_logger(index="transcriber_log",name="transcriber.manager.py")


class Speech2Text:
    def __init__(self):
        self.r = sr.Recognizer()
        self.temp_path = "temp"

    def transcribe_all(self,audio_chunks):
        full_text = []
        for chunk_filename in audio_chunks:
            text = self.transcribe_chunk(chunk_filename)
            full_text.append(text)
        if not full_text:
            raise Exception("Empty transcription.")

        if os.path.isdir(self.temp_path):
            shutil.rmtree(self.temp_path)

        return " ".join(full_text)

    def transcribe_chunk(self,chunk):
        text = ""
        with sr.AudioFile(chunk) as source:
            audio_listened = self.r.record(source)
            try:
                text = self.r.recognize_google(audio_listened)
            except sr.UnknownValueError:
                print(f"Could not understand audio in chunk {chunk}")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
        return text

    def load_and_split(self,audio_path):
        # load audio
        audio = AudioSegment.from_wav(audio_path)
        # split to chunks
        chunks = split_on_silence(audio,
              min_silence_len=500,
              silence_thresh=-40
              )
        return chunks

    def export_chunks(self,chunks):
        temp_files = []
        # if temp files already exist delete the prev files
        if os.path.isdir(self.temp_path):
            shutil.rmtree(self.temp_path)
        #create a temp folder
        os.mkdir(self.temp_path)

        for i, chunk in enumerate(chunks):
            try:
                # Export chunk to a temporary file
                chunk_filename = f"temp/chunk{i}.wav"
                chunk.export(chunk_filename, format="wav")
                temp_files.append(chunk_filename)
            except Exception as e:
                print("error:",e)
        return temp_files


t2s = Speech2Text()
chunky = t2s.load_and_split(r"C:\Users\Yaakov\PycharmProjects\muezzin\data\podcasts\download (2).wav")
print("chunky:",chunky)
chunky_file_list = t2s.export_chunks(chunky)
print("chunky_file_list:",chunky_file_list)
full_transcription = t2s.transcribe_all(chunky_file_list)
print("full_transcription:",full_transcription)
