from flask import Flask, render_template, url_for
from external_services import dark_sky
from services import geolocation

from forecast_dictionary import forecast_dictionary

app = Flask(__name__)


@app.route('/')
def get_current_weather():
    coordinates = geolocation.coordinates_from_ip()
    forecast = dark_sky.proxy.get_current_forecast(coordinates.latitude, coordinates.longitude)
    forecast_dictionary_value = forecast_dictionary[forecast.weather.value]

    image_url = url_for('static', filename=forecast_dictionary_value['image_url'])
    title = forecast_dictionary_value['title']
    is_doing_sport = forecast_dictionary_value['is_doing_sport']

    return render_template('index.html', title=title, image_url=image_url, is_doing_sport=is_doing_sport)


if __name__ == '__main__':
    app.run()
