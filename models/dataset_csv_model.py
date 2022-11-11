from dataclasses import dataclass

from enums.season import Season
from enums.weather_situation import WeatherSituation


@dataclass
class DatasetCsvModel:
    id: int
    season: Season

    # year (0: 2011, 1:2012)
    year: int

    month: int
    hour: int
    weekday: int
    working_day: bool
    weather_situation: WeatherSituation

    # Normalized temperature in Celsius. The values are derived via (t-t_min)/(t_max-t_min), t_min=-8, t_max=+39 (
    # only in hourly scale)
    temperature: float

    # Normalized feeling temperature in Celsius. The values are derived via (t-t_min)/(t_max-t_min), t_min=-16,
    # t_max=+50 (only in hourly scale)
    feeling_temperature: float

    # Normalized humidity. The values are divided to 100 (max)
    humidity: float

    # Normalized wind speed. The values are divided to 67 (max)
    windspeed: float

    casual_users: int
    registered_users: int
    total_users: int
