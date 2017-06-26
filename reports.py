import csv


def reading_text(file_name):
    games_list = list(csv.reader(open(file_name, 'r'), delimiter="\t"))
    return games_list


def count_games(file_name):
    number_of_games = len(reading_text(file_name))
    return number_of_games


print(count_games("game_stat.txt"))


def decide(file_name, year):
    result = any(str(year) in lists for lists in reading_text(file_name))
    return result

print(decide("game_stat.txt", 1999))


def get_latest(file_name):
    sorted_list = sorted(reading_text(file_name), key=lambda x: x[2], reverse=True)
    return sorted_list[0][0]


print(get_latest("game_stat.txt"))


def count_by_genre(file_name, genre):
    counter = 0
    for lists in reading_text(file_name):
        for element in lists:
            if element == genre:
                counter += 1
    return counter


print (count_by_genre("game_stat.txt", "Real-time strategy"))


def get_line_number_by_title(file_name, title):
    import_file = reading_text(file_name)
    for lists in import_file:
        if lists[0] == title:
            return import_file.index(lists)+1

        raise ValueError
        print("Title not in the list")


print(get_line_number_by_title("game_stat.txt", "hehe")


def sort_abc(file_name):
    pass


def get_genres(file_name):
    pass


def when_was_top_sold_fps(file_name):
    pass
