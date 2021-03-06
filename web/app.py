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
from api.wiki import search_wiki
from api.weather import Weather
from api.piCam import captureAndUpdateLink
from api import lightcontroller as lc
import os

app = Flask(__name__)

tts = TextToSpeech()
bustimings= BusTimings()
traffic = Traffic()
psir = PSIReader()
weatherObj = Weather()

TTS_BLUEMIX = 'TTS_BLUEMIX'
TTS_GOOGLE = 'TTS_GOOGLE'
WEB_SETTINGS = {'TTS_TYPE' : TTS_GOOGLE}

piImg =  '/home/pi/homepi/cam.jpg'
piImgSl = '/home/pi/workspace/piHome/web/static/current.jpg'

piPicPreAlert = 'Taking Picture 1 2 3 Go'

ROOM_RELAYS = {'bedroom': lc.Room.Bedroom, 'livingroom': lc.Room.Livingroom, 'bathroom': lc.Room.Bathroom, 'kitchen': lc.Room.Kitchen, 'all': 4}
LIGHT_STATES = {'off': lc.LightState.off, 'on': lc.LightState.on}

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
    __playAudio('pipicprealert.wav',piPicPreAlert)
    text = captureAndUpdateLink(piImg, piImgSl)
    audioFile = 'picam.wav'
    __playAudio(audioFile,text)
    return text

@app.route('/home/<value>')
def home(value):

    switchONOFF = request.args['param']

    state = LIGHT_STATES[switchONOFF]
    lamp = ROOM_RELAYS[value]
    lc.LIGHTS[lamp].switch(state)

    text = 'Switch %s %s light. ' % (switchONOFF, value)
    audioFile = 'home.wav'
    __playAudio(audioFile,text)
    return text.upper();

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
    text = 'No updates'
    if value == 'TODAY':
        text = weatherObj.get_today_text()
    elif value == 'TOMORROW':
        text = weatherObj.get_tomo_text()
    audioFile = 'weather.wav'
    __playAudio(audioFile,text)
    return text

@app.route('/wiki/<value>')
def wiki(value):
    text = search_wiki(value)
    audioFile = 'wiki.wav'
    __playAudio(audioFile,text)
    return text

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