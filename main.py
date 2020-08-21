#import library
import time
import os
import speech_recognition as sr
from pydub import AudioSegment 
from pydub.silence import split_on_silence 


class Speech_to_text:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def speech_to_text_v1(self , path):
        """
        fucntion to convert speech to text

            Parameters:
                path (str) : path to your file
        """
        with sr.AudioFile(path) as source:
            audio_text = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio_text , language='en-IN')
                print(text)
            except:
                print('[INFO] sorry run again....')

    def silent_based_conversion(self , path):
        """
        a function that splits the audio file into chunks 

            Parameters:
                path (str) : path to your file
        """
        audio = AudioSegment.from_wav(path)

        fh = open('recognized.txt' , "w+")

        chunks = split_on_silence(audio ,min_silence_len = 500 , silence_thresh = -20)

        #directory to store
        try:
            os.mkdir('audio_chunks')
        except (FileExistsError):
            pass

        os.chdir('audio_chunks')

        i=0

        for chunk in chunks:

            chunk_silent = AudioSegment.silent(duration = 10)
            audio_chunk = chunk_silent + chunk + chunk_silent
            print(f'[INFO] saving chunk{i}.wav')
            audio_chunk.export(f"./chunk{i}.wav" , bitrate = '128k' , format = 'wav')
            filename = 'chunk'+str(i)+'.wav'
            print(f'[INFO] Processing chunk {i}')
            file = filename
            r = sr.Recognizer() 
		# recognize the chunk 
            with sr.AudioFile(file) as source: 
                audio_text = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio_text , language='en-IN')
                fh.write(text+'.')
            except:
                print('[INFO] sorry run again....')

            i += 1

        os.chdir('..')




if __name__ == "__main__":
    s2t = Speech_to_text()
    # s2t.speech_to_text_v1('chunk85.wav')
    s2t.silent_based_conversion('audio_files/deep_interview.wav')

 
