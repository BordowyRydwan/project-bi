from modules.preparation import data_prepare


if __name__ == '__main__':
    for row in data_prepare.get_data():
        print(row)
