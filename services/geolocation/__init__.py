import geocoder
from models import Coordinates


def coordinates_from_ip() -> Coordinates:
    position = geocoder.ip('me')
    return Coordinates(position.lat, position.lng)
