import requests
import urllib
import time
import os
from email.utils import encode_rfc2231
 
class TextToSpeech:
 
    __proxies = {"http": ""}
    __bmttsHeaders = {'Authorization' : 'Basic YmZiMWY0MzUtZjc3MC00OThjLWJlNDYtNjVmZTE0ZTFjMjc2Ok9KWGVGbWhJeG4xWA=='}
    __blumeixTTSURL =  "https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize?accept=audio/wav&text=%s&voice=en-US_AllisonVoice"
    __googleTTSURL = 'http://translate.google.com/translate_tts?ie=UTF-8&total=1&idx=0&textlen=32&client=tw-ob&q=%s&tl=EN-gb'
    
    def bluemixTTS(self, text, filePath):
        try:
            print 'bluemixTTS : ' + text
            finalText = encode_rfc2231(text, 'utf-8')
            finalText = finalText.replace("utf-8", "")
            #print finalText
            finalurl = TextToSpeech.__blumeixTTSURL % finalText
            #print finalurl
 
            r = requests.get(finalurl,headers=TextToSpeech.__bmttsHeaders, verify=False)
            #print r.status_code
            #print r.headers
            with open(filePath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk: # filter out keep-alive new chunks
                        f.write(chunk)
                        #f.flush() commented by recommendation from J.F.Sebastian
                print 'Done reading'
                f.close()
            r.close()
        except ImportError:
            print 'error'
 
    def googleTTS(self,text, filePath):
        try:

            print 'googleTTS : ' + text
            finalText = encode_rfc2231(text, 'utf-8')
            finalText = finalText.replace("utf-8", "")
            #finalText = urllib.quote(finalText)
            #print finalText
            finalurl = TextToSpeech.__googleTTSURL % finalText
            #print finalurl
 
            r = requests.get(finalurl,
                         proxies=TextToSpeech.__proxies,
                         verify=False)
            #print r.status_code
            #print r.headers
            with open(filePath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk: # filter out keep-alive new chunks
                        f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
                f.close()
            r.close()
 
 
        except ImportError:
            print 'error'

    def play(self, filePath):
        os.system('omxplayer %s' % filePath)
 
if __name__=="__main__":
    tts = TextToSpeech()
    audioFile = 'voice.wav'
    tts.bluemixTTS("I am done for the day blue mix", audioFile)
    #tts.googleTTS("I am done for the day google", audioFile)
    tts.play(audioFile)
    
