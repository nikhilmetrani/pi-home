__author__ = 'jagadeesh'
from flask import Flask, render_template, request
from api.texttospeech import TextToSpeech
#from api import PSIReader
from api.bustimings import BusTimings
import os

app = Flask(__name__)

tts = TextToSpeech()
bustimings= BusTimings()
#psir = PSIReader()

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
    return value

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5001)

