import argparse
from src import fileutils, validator, metrics


def validate_and_transform(data_list):
    ret_val = list()
    for row in data_list:
        date = row['time_data']
        is_valid = validator.verify_date_format(date)
        if is_valid:
            pass
        else:
            new_time_data = {'time_data':
                             validator.transform_date(date)}
            row.update(new_time_data)
        ret_val.append(row)
    return ret_val


def get_metrics(data_list):
    # TODO make this generic
    age_data = list()
    abv_data = list()
    price_data = list()

    for row in data_list:
        if row.get('age'):
            age_data.append(float(row.get('age')))
        if row.get('abv'):
            abv_data.append(float(row.get('abv')))
        if row.get('price'):
            price_data.append(float(row.get('price')))
    if age_data:
        mean_age = metrics.compute_avg(age_data)
    if abv_data:
        mean_abv = metrics.compute_avg(abv_data)
    if price_data:
        mean_price = metrics.compute_avg(price_data)
    metric_data = {'mean_age': mean_age, 'mean_abv': mean_abv, 'mean_price': mean_price}
    for row in data_list:
        row.update(metric_data)
    return data_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Whiskey Parser',
        description='Parses a csv file,'
                    'validates some items then'
                    'transforms them')
    parser.add_argument('--filename')
    args = parser.parse_args()

    data = fileutils.openfile(args.filename)
    data = validate_and_transform(data)
    data = get_metrics(data)
    fileutils.write_csv_file('output.csv', data)
    fileutils.write_parquet_file('output.parquet', data)