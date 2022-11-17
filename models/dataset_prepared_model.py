from dataclasses import dataclass


@dataclass
class DatasetPreparedModel:
    id: int
    season: int

    # year (0: 2011, 1:2012)
    year: int

    month: int
    hour: int
    weekday: int
    holiday: bool
    working_day: bool
    weather_situation: int

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

    # ADDITIONAL VARIABLES
    casual_users_fraction: float
    registered_users_fraction: float
    weekday_normalized: float
    hour_normalized: float
    weather_situation_normalized: float


