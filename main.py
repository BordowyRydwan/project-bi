from modules.preparation import prepare_data, csv_data

if __name__ == '__main__':
    csv = csv_data.get()
    prepared_data = prepare_data.model_list(csv)
    csv_data.write(prepared_data)

