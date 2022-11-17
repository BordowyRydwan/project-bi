from typing import List

from models.dataset_csv_model import DatasetCsvModel
from models.dataset_prepared_model import DatasetPreparedModel
from numpy import mean

MAX_WEEKDAY = 6
MAX_HOUR = 23
MAX_WEATHER_SITUATION = 4


def model(csvModel: DatasetCsvModel, avg: float) -> DatasetPreparedModel:
    return DatasetPreparedModel(
        csvModel.id,
        csvModel.season,
        csvModel.year,
        csvModel.month,
        csvModel.hour,
        csvModel.weekday,
        csvModel.holiday,
        csvModel.working_day,
        csvModel.weather_situation,
        csvModel.temperature,
        csvModel.feeling_temperature,
        csvModel.humidity,
        csvModel.windspeed,
        csvModel.casual_users,
        csvModel.registered_users,
        csvModel.total_users,
        round(csvModel.casual_users / csvModel.total_users, 4),
        round(csvModel.registered_users / csvModel.total_users, 4),
        round(csvModel.weekday / MAX_WEEKDAY, 4),
        round(csvModel.hour / MAX_HOUR, 4),
        round((csvModel.weather_situation - 1) / (MAX_WEATHER_SITUATION - 1), 4),
        1 if csvModel.total_users > avg else 0
    )


def model_list(csvModelList: List[DatasetCsvModel]) -> List[DatasetPreparedModel]:
    avg = mean(list(map(lambda x: x.total_users, csvModelList)))
    result = []

    for item in csvModelList:
        result.append(model(item, avg))

    return result
