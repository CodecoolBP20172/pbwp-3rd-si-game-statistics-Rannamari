import csv


def reading_text(file_name):
    games_list = list(csv.reader(open(file_name, 'r'), delimiter="\t"))
    return games_list


def get_most_played(file_name):
    sorted_list = sorted(reading_text(file_name), key=lambda x: float(x[1]), reverse=True)
    return sorted_list[0][0]


def get_specific_data_from_file(file_name, cast_funct, index):
    new_list = []
    for lists in reading_text(file_name):
        new_list.append(cast_funct(lists[index]))
    return new_list


def get_selling_avg(file_name):
    return sum(get_specific_data_from_file(file_name, float, 1))/float(len(get_specific_data_from_file(file_name, float, 1)))


def sum_sold(file_name):
    return sum(get_specific_data_from_file(file_name, float, 1))


def count_longest_title(file_name):
    return sorted(get_specific_data_from_file(file_name, len, 0), reverse=True)[0]


def get_date_avg(file_name):
    return round(sum(get_specific_data_from_file(file_name, int, 2))/float(len(get_specific_data_from_file(file_name, int, 2))))


def isfloat(x):
    try:
        a = float(x)
    except ValueError:
        return False
    else:
        return True


def isint(x):
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b


def get_game(file_name, title):
    title_item_list = []
    for lists in reading_text(file_name):
        if lists[0] == title:
            for items in lists:
                if isint(items):
                    items = int(items)
                elif isfloat(items):
                    items = float(items)
                title_item_list.append(items)
            return title_item_list
