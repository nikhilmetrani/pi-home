__author__ = 'tester'
import urllib3
import urllib3.request
import json
from dateutil import parser
import datetime
import time
from texttospeech import TextToSpeech

class BusTimings:

    __http = urllib3.PoolManager()
    __headers = {'AccountKey':'rvXT5s1ZSSKldpkizIhlag==','UniqueUserID':'984004a4-2685-4b30-8514-b3a75513c2bd', 'accept':'application/json'}

    def getBusInformation(self,busStopId, serviceNo, busStopName='Your'):
        print   'BusStopID=%s , ServiceNo=%s, busStopName=%s' % (busStopId, serviceNo, busStopName)
        r = BusTimings.__http.request('GET', 'http://datamall2.mytransport.sg/ltaodataservice/BusArrival?BusStopID='+str(busStopId)+'&SST=True&ServiceNo='+str(serviceNo), headers=BusTimings.__headers)
        #print r.status
        #print r.data

        jsonObj = json.loads(r.data)
        r.close()
        #print json.dumps(jsonObj, sort_keys=True, indent=4)

        #print jsonObj['Services'][0]['NextBus']
        #print jsonObj['Services'][0]['SubsequentBus']
        #print jsonObj['Services'][0]['SubsequentBus3']

        cdt = datetime.datetime.now()

        firstBusArrivalDateTime = parser.parse(jsonObj['Services'][0]['NextBus']['EstimatedArrival'])
        SecondBusArrivalDateTime = parser.parse(jsonObj['Services'][0]['SubsequentBus']['EstimatedArrival'])
        thirdBusArrivalDateTime = parser.parse(jsonObj['Services'][0]['SubsequentBus3']['EstimatedArrival'])

        firstBusLoad = jsonObj['Services'][0]['NextBus']['Load']
        secondBusLoad = jsonObj['Services'][0]['SubsequentBus']['Load']

        firstBusInMins = (int(time.mktime(firstBusArrivalDateTime.timetuple())) - int(time.time())) / 60
        secondBusInMins = (int(time.mktime(SecondBusArrivalDateTime.timetuple())) - int(time.time())) / 60
        thirdBusInMins = (int(time.mktime(thirdBusArrivalDateTime.timetuple())) - int(time.time())) / 60

        message = '%s bus at %s bus stop, you have' % (serviceNo, busStopName)

        if firstBusInMins <= 0:
            message = '%s First Bus Arrived with %s.' % (message, firstBusLoad)
        else:
            message = '%s First Bus Arriving in %s minutes with %s.' % (message, firstBusInMins, firstBusLoad)

        if secondBusInMins <= 0:
            message = '%s Second Bus Arrived with %s. ' % (message, secondBusLoad)
        else:
            message = '%s Second Bus Arriving in %s minutes with %s.' % (message, secondBusInMins, secondBusLoad)

        if thirdBusInMins >= 0:
            message = '%s Third Bus Arriving in %s minutes.' % (message, thirdBusInMins)

        print message
        return message
        #print 'you have First %s bus in %s mins it got %s, Second one in %s mins with %s and third one in %s mins' %
        # (serviceNo, firstBusInMins, firstBusLoad, secondBusInMins,secondBusLoad,thirdBusInMins)


if __name__=="__main__":

    bus = BusTimings()
    message = bus.getBusInformation(96129, 20, 'Melville Park')
    tts = TextToSpeech()
    audioFile = 'bus.wav'
    tts.bluemixTTS(message, audioFile)
    #tts.googleTTS("I am done for the day google", audioFile)
    tts.play(audioFile)
    
    #getBusInformation(96371, 20, 'SCB CBP')
    #getBusInformation(96319, 20, 'Yusen Logistics')
