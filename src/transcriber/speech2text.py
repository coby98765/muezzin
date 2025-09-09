from pydub.silence import split_on_silence
from src.utils.logger import Logger
import speech_recognition as sr
from pydub import AudioSegment
from datetime import datetime
import shutil
import os


# logger setup
logger = Logger.get_logger(index="transcriber_log",name="transcriber.manager.py")


class Speech2Text:
    def __init__(self):
        self.r = sr.Recognizer()
        self.temp_path = "temp"
        logger.info(f'Speech2Text.init, Setup Complete.')

    def transcribe_all(self,audio_chunks):
        full_text = []
        for chunk_filename in audio_chunks:
            text = self.transcribe_chunk(chunk_filename)
            full_text.append(text)
        if not full_text:
            logger.error(f"Speech2Text.transcribe_all, Empty transcription.")
            raise Exception("Empty transcription.")

        if os.path.isdir(self.temp_path):
            shutil.rmtree(self.temp_path)
        logger.info(f'Speech2Text.transcribe_all, file transcription complete.')
        return " ".join(full_text)

    def transcribe_chunk(self,chunk):
        text = ""
        with sr.AudioFile(chunk) as source:
            audio_listened = self.r.record(source)
            try:
                text = self.r.recognize_google(audio_listened)
                #sphinx works offline but not perfect
                # text = self.r.recognize_sphinx(audio_listened)
            except sr.UnknownValueError:
                Speech2Text.handel_corrupted_chunk(chunk)
                logger.error(f"Speech2Text.transcribe_chunk, Could not understand audio in chunk {chunk}.")
            except sr.RequestError as e:
                logger.error(f"Speech2Text.transcribe_chunk, Could not request results from Google Speech Recognition service; {e}.")
                raise Exception(e)

        return text

    def load_and_split(self,audio_path):
        logger.info(f'Speech2Text.load_and_split, beginning transcription for file: {audio_path}.')
        # load audio
        audio = AudioSegment.from_wav(audio_path)
        # split to chunks
        chunks = split_on_silence(audio,
              min_silence_len=600,
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
                logger.error(f"Speech2Text.transcribe_all, error: {e}.")
                raise Exception(e)
        return temp_files

    @staticmethod
    def handel_corrupted_chunk(corrupted):
        corrupted_dir = "corrupted"
        if not os.path.isdir(corrupted_dir):
            os.mkdir(corrupted_dir)

        destination_file_name = f"debug_{datetime.now().strftime("%Y%m%d_%H%M%S%f")}.wav"
        # shutil.copy(corrupted, destination_file_name)
        shutil.copy2(corrupted, fr"{corrupted_dir}/{destination_file_name}")

        logger.debug(f"Speech2Text.handel_corrupted_chunk, corrupted file saved to: {destination_file_name}.")

