import csv


def reading_text(file_name):
    games_list = list(csv.reader(open(file_name, 'r'), delimiter="\t"))
    return games_list


def get_most_played(file_name):
    sorted_list = sorted(reading_text(file_name), key=lambda x: float(x[1]), reverse=True)
    return sorted_list[0][0]


def iterating(file_name, math, number):
    new_list = []
    for lists in reading_text(file_name):
        new_list.append(math(lists[number]))
    return new_list


def get_selling_avg(file_name):
    return sum(iterating(file_name, float, 1))/float(len(iterating(file_name, float, 1)))


def sum_sold(file_name):
    return sum(iterating(file_name, float, 1))


def count_longest_title(file_name):
    return sorted(iterating(file_name, len, 0), reverse=True)[0]



def get_date_avg(file_name):
    avg_years = []
    for lists in reading_text(file_name):
        avg_years.append(int(lists[2]))
    return round(sum(avg_years)/float(len(avg_years)))

def get_game(file_name, title):
    title_item_list = []
    for lists in reading_text(file_name):
        if lists[0] == title:
            for items in lists:
                try:
                    items = int(items)
                    title_item_list.append(items)
                except ValueError:
                    title_item_list.append(items)
            return title_item_list
