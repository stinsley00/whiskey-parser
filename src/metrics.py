from decimal import Decimal
from statistics import mean


def compute_avg(data_list: list):
    return round(Decimal(mean(data_list)), 2)


def count_items(data_list: list):
    return sum(data_list)

