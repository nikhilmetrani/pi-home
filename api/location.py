import json,urllib,requests


def get_current_location():
    key = "AIzaSyBouh6FWJfByRmwF670XU_pkDy_ct854ZY" #Google API Key
    geoUrl = "https://www.googleapis.com/geolocation/v1/geolocate?key=" + key
    payload = {'considerIp': 'true'}
    response = requests.post(geoUrl, data = json.dumps(payload))
    res_json = response.json()
    location = res_json[u'location']
    lat = location[u'lat']
    lng = location[u'lng']
    accuracy = res_json[u'accuracy']
    return (lat, lng, accuracy)
