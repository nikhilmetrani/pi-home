__author__ = 'jagadeesh'
from flask import Flask, render_template, request
from api.texttospeech import TextToSpeech
#from api import PSIReader
from api.bustimings import BusTimings
from api.news import get_news_by_category
import os

app = Flask(__name__)

tts = TextToSpeech()
bustimings= BusTimings()
#psir = PSIReader()

TTS_BLUEMIX = 'TTS_BLUEMIX'
TTS_GOOGLE = 'TTS_GOOGLE'
WEB_SETTINGS = {'TTS_TYPE' : TTS_GOOGLE}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/airquality/<value>')
def airquality(value):
    text = value
    '''
    text = psir.getPSIMessage(value, request.args['param'])
    audioFile = 'psi.wav'
    tts.bluemixTTS(text, audioFile)
    #tts.googleTTS(text, audioFile)
    tts.play(audioFile)
    '''
    return text


@app.route('/bus/<value>')
def bus(value):
    text = bustimings.getBusInformation(96129, value, busStopName='Your')
    audioFile = 'bustimings.wav'
    tts.bluemixTTS(text, audioFile)
    #tts.googleTTS(text, audioFile)
    tts.play(audioFile)
    return text    

@app.route('/picamera/<value>')
def camerapi(value):
    return value

@app.route('/home/<value>')
def home(value):
    return value + request.args['param']

@app.route('/news/<value>')
def news(value):
    newsList = get_news_by_category(value)
    for news in newsList:
        print news
        __playAudio('news.wav',news)

    return "NEWS Done !!"

@app.route('/traffic/<value>')
def traffic(value):
    return '%s %s' % (value, request.args['param'])

@app.route('/weather/<value>')
def weather(value):
    return '%s %s' % (value, request.args['param'])

@app.route('/wiki/<value>')
def wiki(value):
    return value

@app.route('/stopVoice/<value>')
def stopVoice(value):
    os.system('pkill omxplayer')
    return 'Voice Stopped'

@app.route('/settings/<value>')
def settings(value):

    print request.args

    WEB_SETTINGS['TTS_TYPE'] = request.args['ttstype']

    return "Settings saved !!" + request.args['ttstype']

def __playAudio(filePath, text):

    if WEB_SETTINGS['TTS_TYPE'] is TTS_GOOGLE:
        tts.googleTTS(text, filePath)
    else:
        tts.bluemixTTS(text, filePath)

    tts.play(filePath)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5001)

