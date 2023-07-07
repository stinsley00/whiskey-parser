import csv
from uuid import uuid4
import pandas


def openfile(filename: str):
    ret_list = list()
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for cnt, row in enumerate(reader):
            uid = str(uuid4())
            row.update({'row_num': cnt})
            row.update({'id': uid})
            ret_list.append(row)
    return ret_list


def write_csv_file(filename: str, data: list):
    filename = 'output_data/' + filename
    with open(filename, 'w') as outfile:
        headers = data[0].keys()
        writer = csv.DictWriter(outfile, fieldnames=headers, delimiter='|',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(data)


def write_parquet_file(filename: str, data: list):
    filename = 'output_data/' + filename
    df = pandas.DataFrame.from_records(data)
    df.to_parquet(filename)
