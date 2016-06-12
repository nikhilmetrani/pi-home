__author__ = 'jagadeesh'
import urllib3
import urllib3.request
import json

class Traffic:

    __http = urllib3.PoolManager()
    __headers = {'AccountKey':'rvXT5s1ZSSKldpkizIhlag==','UniqueUserID':'984004a4-2685-4b30-8514-b3a75513c2bd', 'accept':'application/json'}
    __sgLTATrafficURL = 'http://datamall2.mytransport.sg/ltaodataservice/TrafficIncidents?$skip=%s'

    def getTraficUpdates(self, type, searchKey):

        skip = 0
        totalRecordsCount = 0
        insidentCount = 0
        insidentMessage = ''

        while True:
            r = Traffic.__http.request('GET', Traffic.__sgLTATrafficURL % skip, headers=Traffic.__headers)
            #print r.status
            #print r.getheaders()
            #print r.data

            jsonObj = json.loads(r.data)
            incidentSet = jsonObj['value']
            resultCount  = len(incidentSet);
            #print 'resultCount = %s' % resultCount
            if resultCount == 0:
                break
            totalRecordsCount = totalRecordsCount + resultCount
            for item in incidentSet:
                print item
                if (type in item['Type']) and (searchKey.lower() in item['Message'].lower()):
                        insidentCount = insidentCount + 1
                        insidentMessage = item['Message']
                        #print item['Type'] + ' -------- ' + item['Message']

            r.close()
            skip = skip + 50

        message = ''

        if insidentCount > 0:
            if insidentCount == 1:
                message = 'There is %s %s incident on %s. %s' % (insidentCount, type, searchKey, insidentMessage)
            else:
                message = 'There are %s %s incidents on %s. %s' % (insidentCount, type, searchKey, insidentMessage)
        else:
            message = 'There is no %s incident on %s' % (type, searchKey)

        #print 'totalRecords=' + str(totalRecordsCount)
        return message

if __name__=="__main__":
    # AYE, KJE, BKE, ORRS, NSE, CTE, KPE, TPE, ECP, PIE, MCE
    # Heavy Traffic, Accident, Diversion, Obstacle, Roadwork, Road block, Misc, Unattended vehicle, Vehicle breakdown, Weather
    traffic = Traffic()
    print traffic.getTraficUpdates('Roadwork','AYE')