__author__ = 'jagadeesh'
from os import path
import sys
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from flask import Flask, render_template, request
from api.texttospeech import TextToSpeech
from api.psireader import PSIReader
from api.bustimings import BusTimings
from api.news import News
from api.traffic import Traffic
import os

app = Flask(__name__)

tts = TextToSpeech()
bustimings= BusTimings()
traffic = Traffic()
psir = PSIReader()

TTS_BLUEMIX = 'TTS_BLUEMIX'
TTS_GOOGLE = 'TTS_GOOGLE'
WEB_SETTINGS = {'TTS_TYPE' : TTS_GOOGLE}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/airquality/<value>')
def airquality(value):
    text = value
    text = psir.getPSIMessage(value, request.args['param'])
    audioFile = 'psi.wav'
    __playAudio(audioFile,text)
    return text


@app.route('/bus/<value>')
def bus(value):
    text = bustimings.getBusInformation(96129, value, busStopName='Your')
    audioFile = 'bustimings.wav'
    __playAudio(audioFile,text)
    return text    

@app.route('/picamera/<value>')
def camerapi(value):
    return value

@app.route('/home/<value>')
def home(value):
    return value + request.args['param']

@app.route('/news/<value>')
def news(value):
    news = News()
    newsList = news.get_news_by_category(value)
    for text in newsList:
        #print news
        __playAudio('news.wav',text)

    return "NEWS Done !!"

@app.route('/trafficIncidents/<value>')
def trafficIncidents(value):


    trafficRoadName = request.args['trafficRoadName']
    searchKey = ''
    if trafficRoadName:
        searchKey = trafficRoadName
    else:
        searchKey = request.args['highway']

    #print searchKey
    audioFile = 'trafficInc.wav'
    text = traffic.getTraficUpdates(request.args['incidentType'], searchKey)
    __playAudio(audioFile,text)
    return text

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
    #print request.args
    WEB_SETTINGS['TTS_TYPE'] = request.args['ttstype']
    return "Settings saved !!"

@app.route('/texttospeech')
def texttospeech():
    text = request.args['message']
    audioFile = 'texttospeech.wav'
    __playAudio(audioFile,text)
    return "Played your Text !!"


def __playAudio(filePath, text):

    if WEB_SETTINGS['TTS_TYPE'] is TTS_GOOGLE:
        tts.googleTTS(text, filePath)
    else:
        tts.bluemixTTS(text, filePath)

    tts.play(filePath)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5001)

