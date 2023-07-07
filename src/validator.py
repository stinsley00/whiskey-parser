import re
from datetime import datetime


def transform_date(date):
    try:
        transformed_dt = datetime.strptime(date, '%m-%d-%Y %H:%M:%S')
        return transformed_dt.strftime('%Y-%d-%m  %H:%M:%S')
    except ValueError as ve:
        raise ve


def verify_date_format(date_to_test: str):
    """verify date is in appropriate format"""
    regex = r'^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$'
    matcher = re.match
    return matcher(regex, date_to_test)


