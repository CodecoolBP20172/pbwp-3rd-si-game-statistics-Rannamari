import csv
from collections import Counter
from itertools import *


def reading_text(file_name):
    games_list = list(csv.reader(open(file_name, 'r'), delimiter="\t"))
    return games_list


def get_most_played(file_name):
    sorted_list = sorted(reading_text(file_name), key=lambda x: float(x[1]), reverse=True)
    return sorted_list[0][0]


def get_specific_data_from_file(file_name, cast_funct, index):
    new_list = []
    for data_list in reading_text(file_name):
        new_list.append(cast_funct(data_list[index]))
    return new_list


def get_selling_avg(file_name):
    return sum(get_specific_data_from_file(file_name, float, 1))/float(len(get_specific_data_from_file(file_name, float, 1)))


def sum_sold(file_name):
    return sum(get_specific_data_from_file(file_name, float, 1))


def count_longest_title(file_name):
    return sorted(get_specific_data_from_file(file_name, len, 0), reverse=True)[0]


def get_date_avg(file_name):
    return round(sum(get_specific_data_from_file(file_name, int, 2))/float(len(get_specific_data_from_file(file_name, int, 2))))


def is_float(item):
    try:
        float_number = float(item)
    except ValueError:
        return False
    else:
        return True


def is_int(item):
    try:
        float_number = float(item)
        int_number = int(float_number)
    except ValueError:
        return False
    else:
        return float_number == int_number


def get_game(file_name, title):
    title_item_list = []
    for data_list in reading_text(file_name):
        if data_list[0] == title:
            for item in data_list:
                if is_int(item):
                    item = int(item)
                elif is_float(item):
                    item = float(item)
                title_item_list.append(item)
            return title_item_list


def append_to_list(file_name, index):
    new_list = []
    for data_list in reading_text(file_name):
        new_list.append(data_list[index])
    return new_list


def count_grouped_by_genre(file_name):
    append_to_list(file_name, 3)
    return dict(Counter(append_to_list(file_name, 3)))
