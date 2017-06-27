from reports import *
# exporting files from reports.py to a newly created txt file


def export_data(file_name):
    with open(file_name, 'w', newline="\n") as file:
            file.writelines(str(count_games("game_stat.txt"))+"\n")
            file.writelines(str(decide("game_stat.txt", 2004))+"\n")
            file.writelines(str(get_latest("game_stat.txt"))+"\n")
            file.writelines(str(count_by_genre("game_stat.txt", "Real-time strategy"))+"\n")
            file.writelines(str(get_line_number_by_title("game_stat.txt", "Minecraft"))+"\n")
            file.writelines(str(sort_abc("game_stat.txt"))+"\n")
            file.writelines(str(get_genres("game_stat.txt"))+"\n")
            file.writelines(str(when_was_top_sold_fps("game_stat.txt")))


export_data()
