from enum import Enum


class Weather(Enum):
    CLEAR_DAY = 'clear-day'
    CLEAR_NIGHT = 'clear_night'
    RAIN = 'rain'
    SNOW = 'snow'
    SLEET = 'sleet'
    WIND = 'wind'
    FOG = 'fog'
    CLOUDY = 'cloudy'
    PARTY_CLOUD_DAY = 'party_cloud_day'
    UNAVAILABLE = 'unavailable'

    @classmethod
    def from_value(cls, value: str):
        for weather in Weather:
            if weather.value == value:
                return weather
        return Weather.UNAVAILABLE
