import forecastio
import location
import datetime

forecastio_api_key = "e878ebfb137a31a67ce9b0bc07fde71b"


class Weather:
    def __init__(self, params=None):
        if params is None:
            self.api_key = forecastio_api_key
        else:
            self.api_key = params["WEATHER_API_KEY"]

    def get_forecast(self, time=None):
        (lat, lng, accuracy) = location.get_current_location()
        if time is None:
            forecast = forecastio.load_forecast(self.api_key, lat, lng)
        else:
            forecast = forecastio.load_forecast(self.api_key, lat, lng, time=time)
        return forecast

    def get_today_text(self):
        forecast = self.get_forecast()
        return self.format_text_today(forecast)

    def get_tomo_text(self):
        forecast = self.get_forecast()
        return self.format_text_tomo(forecast)

    @staticmethod
    def format_text_today(forecast):
        text = ''
        currently = forecast.currently()
        temp = None
        if currently is not None:
            temp = currently.d['temperature']
            text += 'The temperature now is {temp} degrees. {summary}. '.format(temp=temp,
                                                                                summary=currently.summary)
        hourly = forecast.hourly()
        text += hourly.summary
        if hourly.icon == u'rain':
            text += 'Do not forget to take an umbrella while going outside.'
        elif temp > 35:
            text += 'Stay indoors or apply sunscreen when going outside.'
        return text

    @staticmethod
    def format_text_tomo(forecast):
        text = ''
        daily = forecast.daily()
        tomo = datetime.date.today() + datetime.timedelta(days=1)
        filtered_data = filter(lambda x: x.time.date() == tomo, daily.data)
        if filtered_data.__len__() != 0:
            tomo_data = filtered_data[0]
            min_temp = tomo_data.d[u'temperatureMin']
            max_temp = tomo_data.d[u'temperatureMax']
            icon = tomo_data.d[u'icon']
            summary = tomo_data.d[u'summary']
            text += 'Temperature will be between {min_temp} and {max_temp} degrees. {summary} ' \
                .format(min_temp=min_temp, max_temp=max_temp, summary=summary)
            if icon == u'rain':
                text += 'Do not forget to take an umbrella while going outside.'
            elif max_temp > 35:
                text += 'Stay indoors or apply sunscreen when going outside.'
        return text
