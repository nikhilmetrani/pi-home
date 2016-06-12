import forecastio, json

forecastio_ap_key = "e878ebfb137a31a67ce9b0bc07fde71b"

def get_forecast(lat, lng):
    return forecastio.load_forecast(forecastio_ap_key, lat, lng)

def get_forecast_text(lat, lng):
    forecast = get_forecast(lat, lng)
    currently_text = get_currently_text(forecast.currently())
    hourly_text = get_hourly_text(forecast.hourly())
    daily_text = get_daily_text(forecast.daily())
    return '%(currently)s %(hourly)s %(daily)s' % { "currently" : currently_text, "hourly" : hourly_text, "daily" : daily_text}

def get_currently_text(currently):
    return 'currently'

def get_hourly_text(hourly):
    return 'hourly'

def get_daily_text(daily):
    return 'daily'