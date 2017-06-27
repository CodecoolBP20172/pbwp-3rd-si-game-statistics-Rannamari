import csv


def reading_text(file_name):
    games_list = list(csv.reader(open(file_name, 'r'), delimiter="\t"))
    return games_list


def get_most_played(file_name):
    sorted_list = sorted(reading_text(file_name), key=lambda x: float(x[1]), reverse=True)
    return sorted_list[0][0]


def sum_sold(file_name):
    sold_games = []
    for lists in reading_text(file_name):
        sold_games.append(float(lists[1]))
    return (sum(sold_games))


def get_selling_avg(file_name):
    sold_games = []
    for lists in reading_text(file_name):
        sold_games.append(float(lists[1]))
    return sum(sold_games)/float(len(sold_games))


def count_longest_title(file_name):
    title_list = []
    for lists in reading_text(file_name):
        title_list.append(len(lists[0]))
    sorted_title_list = sorted(title_list, reverse=True)
    print(sorted_title_list)
    return sorted_title_list[0]


def get_date_avg(file_name):
    avg_years = []
    for lists in reading_text(file_name):
        avg_years.append(int(lists[2]))
    return round(sum(avg_years)/float(len(avg_years)))


def get_game(file_name, title):
    for lists in reading_text(file_name):
        if lists[0] == title:
            return lists
