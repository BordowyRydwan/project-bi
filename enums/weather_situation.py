from enum import Enum


class WeatherSituation(str, Enum):
    # Clear, Few clouds, Partly cloudy, Partly cloudy
    CLEAR = 1

    # Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
    CLOUDY = 2

    # Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
    RAINING = 3

    # Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
    HEAVY_RAINING = 4
