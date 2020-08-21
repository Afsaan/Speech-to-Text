#import library
import time
import speech_recognition as sr


class Speech_to_text():
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def speech_to_text_v1(self , path):
        """
        """
        with sr.AudioFile(path) as source:
            audio_text = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio_text , language='en-IN')
                print(text)
            except:
                print('[INFO] sorry run again....')

    def silent_based_conversion(self , path)

if __name__ == "__main__":
    s2t = Speech_to_text()
    s2t.speech_to_text_v1('test1.wav')

# # Initialize recognizer class (for recognizing the speech)
# r = sr.Recognizer()

# # Reading Audio file as source
# # listening the audio file and store in audio_text variable

# start_time = time.time()

# with sr.AudioFile('test1.wav') as source:
    
#     audio_text = r.listen(source)
    
# # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
#     try:
        
#         # using google speech recognition
#         text = r.recognize_google(audio_text, language="en-IN")
#         print('Converting audio transcripts into text ...')
#         print(text)
#         print(((time.time())-start_time))
     
#     except:
#          print('Sorry.. run again...')

 
