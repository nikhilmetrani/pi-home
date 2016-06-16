web:
    sudo pip install Flask
    sudo apt-get install python-lxml
    sudo pip install urllib3

    # instal six only if needed used in BusTimings module for dateutil
    sudo pip install six
    sudo pip install wikipedia

    #to kill process holding port
    sudo netstat -nlp | grep :5001