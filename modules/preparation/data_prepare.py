from typing import List, Dict

from dataclass_csv import DataclassReader
from models.dataset_csv_model import DatasetCsvModel
from consts.filenames import HOUR_DATASET_FILENAME

mappings: Dict[str, str] = {
    'instant': 'id',
    'yr': 'year',
    'mnth': 'month',
    'hr': 'hour',
    'workingday': 'working_day',
    'weathersit': 'weather_situation',
    'temp': 'temperature',
    'atemp': 'feeling_temperature',
    'hum': 'humidity',
    'atemp': 'feeling_temperature',
    'casual': 'casual_users',
    'registered': 'registered_users',
    'cnt': 'total_users'
}


def map_reader(reader: DataclassReader) -> None:
    for (key, value) in mappings.items():
        reader.map(key).to(value)


def get_data() -> List[DatasetCsvModel]:
    filename = HOUR_DATASET_FILENAME
    result = []

    with open(filename) as days_csv:
        reader = DataclassReader(days_csv, DatasetCsvModel)
        map_reader(reader)

        for row in reader:
            result.append(row)

    return result
