import requests
from lxml import etree
import sys
import logging
from texttospeech import TextToSpeech
 
 
class PSIReader:
 
    __apiURL = 'http://www.nea.gov.sg/api/WebAPI/?dataset=psi_update&keyref=781CF461BB6606ADEA01E0CAF8B35274602B7580279AFE8F'
    __proxies = {"http": 'http://host:port'}
    __xpathTemplate = "/channel/item/region/id[text()='%s']/../record/reading[@type='NPSI']/@value"
 
 
    def __init__(self):
        #print __name__
        global logger
        logger = logging.getLogger('PSIReader')
        hdlr = logging.FileHandler('myapp.log')
        formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr)
        logger.setLevel(logging.INFO)
 
    def getPSIUpdates(self):
 
        try:
            r = requests.get(PSIReader.__apiURL,                         
                         verify=False)
            #print r.status_code
            #print r.headers
            xmlvalue = r.content
            r.close()
            return xmlvalue
        except:
            logger.error('Error', exc_info=True)
   
    @staticmethod  
    def processXML(xmlvalue, regionCode, location):
 
        try:
            root = etree.fromstring(xmlvalue)
            val = root.xpath(PSIReader.__xpathTemplate % regionCode)
            psival = int(val[0])
 
            message = ''
            if psival >=0 and psival <=50:
                message = 'Good'
            elif psival >=51 and psival <=100:
                message = 'Moderate. You can do Normal activities. Stay Healthy'
            elif psival >=101 and psival <=200:
                message = 'Unhealthy. Take Mask. Drink Lot of Water and minimised outdoor activities'
            elif psival >=200 and psival <=300:
                message = 'Very unhealthy. Take Mask and Stay indoor. Drink Lot of Water'
            elif psival >=300:
                message = 'Hazardous. Take Mask and Stay indoor. Drink Lot of Water'
            else:
                return 'Looks like P S I value is not available from source'
        except:
            logger.error("Error: %s" % sys.exc_info()[0], exc_info=True)
            return 'I am sorry, looks like P S I value is not available from source'
 
        return '%s P S I Value is %s and is %s' % (location, psival,message)

    def getPSIMessage(self, regionCode, location):
        xmlValue = self.getPSIUpdates()
        #print xmlValue
        text = self.processXML(xmlValue, regionCode, location)
        #print 'final message %s' % text
        return text
 
if __name__=="__main__":
 
    psiReader = PSIReader()
    xmlValue = psiReader.getPSIUpdates()
    text = psiReader.processXML(xmlValue, 'rNO', 'Singapore North')
    tts = TextToSpeech()
    audioFile = 'psiblue.wav'
    tts.bluemixTTS(text, audioFile)
    #tts.googleTTS("I am done for the day google", audioFile)
    tts.play(audioFile)
    #logger.info(xmlValue)
    print 
    #print psiReader.processXML(xmlValue, 'rWE134', 'Singapore West')
    #print processXML(xmlvalue, 'rCE', 'Singapore Central')
    #print processXML(xmlvalue, 'rWE', 'Singapore West')
    #print processXML(xmlvalue, 'rEA', 'Singapore East')
    #print processXML(xmlvalue, 'rSO', 'Singapore South')
