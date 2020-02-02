from models import Forecast, Weather


def raw_forecast_to_domain_forecast(raw_forecast) -> Forecast:
    TIME_CURRENT = 'currently'

    raw_weather = raw_forecast[TIME_CURRENT]['icon']
    weather = Weather.from_value(raw_weather)

    return Forecast(weather)
