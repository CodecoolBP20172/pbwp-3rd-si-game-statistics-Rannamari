import csv


# reading the given txt file
def reading_text(file_name):
    games_list = list(csv.reader(open(file_name, 'r'), delimiter="\t"))
    return games_list


# counts how many games are in the imported file
def count_games(file_name):
    number_of_games = len(reading_text(file_name))
    return number_of_games


# decides if there is a game produced in the given year
def decide(file_name, year):
    result = any(str(year) in lists for lists in reading_text(file_name))
    return result


# returns the latest game in the file
def get_latest(file_name):
    sorted_list = sorted(reading_text(file_name), key=lambda x: x[2], reverse=True)
    return sorted_list[0][0]


# counts how many games are in the file by genre
def count_by_genre(file_name, genre):
    counter = 0
    for lists in reading_text(file_name):
        for element in lists:
            if element == genre:
                counter += 1
    return counter


# returns the line number of the given title
def get_line_number_by_title(file_name, title):
    for lists in reading_text(file_name):
        if lists[0] == title:
            return (reading_text(file_name).index(lists)+1)
    raise ValueError


# alphabetically sorts the lines in the file without teh sorted()function
def sort_abc(file_name):
    games = []
    for lists in reading_text(file_name):
        games.append(lists[0])
    iteration = 0
    while (iteration < len(games)):
        item = 0
        while item <= len(games)-2:
            if (games[item] > games[item+1]):
                temp = games[item+1]
                games[item+1] = games[item]
                games[item] = temp
                item += 1
            else:
                item += 1
        iteration += 1
    return games


# alphabetically sorts the genres
def get_genres(file_name):
    genres = []
    for lists in reading_text(file_name):
        if lists[3] in genres:
            continue
        else:
            genres.append(lists[3])
    return sorted(genres, key=str.lower)


# returns the date when First-person shooter was released
def when_was_top_sold_fps(file_name):
    top_sold_dict = {}
    for lists in reading_text(file_name):
        if lists[3] == "First-person shooter":
            top_sold_dict.update({float(lists[1]): int(lists[2])})
        else:
            continue
    if not top_sold_dict:
        raise ValueError
        return
    top_sort_dict = sorted(top_sold_dict.items(), key=lambda x: x[0], reverse=True)
    return top_sort_dict[0][1]
