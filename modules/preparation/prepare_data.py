from typing import List

from models.dataset_csv_model import DatasetCsvModel
from models.dataset_prepared_model import DatasetPreparedModel

MAX_WEEKDAY = 6
MAX_HOUR = 23
MAX_WEATHER_SITUATION = 4


def model(csvModel: DatasetCsvModel) -> DatasetPreparedModel:
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
        round((csvModel.weather_situation - 1) / (MAX_WEATHER_SITUATION - 1), 4)
    )


def model_list(csvModelList: List[DatasetCsvModel]) -> List[DatasetPreparedModel]:
    return list(map(model, csvModelList))
