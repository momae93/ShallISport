import requests
from models import Forecast
from .constants import BASE_URL, TOKEN
from .mapper import raw_forecast_to_domain_forecast


def get_current_forecast(latitude, longitude) -> Forecast:
    url = f'{BASE_URL}{TOKEN}/{latitude},{longitude}'

    raw_forecast = requests.get(url).json()

    return raw_forecast_to_domain_forecast(raw_forecast)

