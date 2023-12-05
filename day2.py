# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
from prep_input import *

def find_valid_games():
    id_numbers = []
    criterion_dict ={"red": 12, "green": 13, "blue": 14}

    Lines = prep_input('day2_input.txt')

    for line in Lines:
        game_id = line[:line.index(":")].replace("Game", "")
        split_line = line.replace(":", ";").split(";")

        valid = True
        for handful in split_line[1:]:
            values = [int(i) for i in handful.split() if i.isdigit()]
            colors = [j.replace(",", "") for j in handful.split() if j.isdigit() == False]
            for x in range(len(colors)):
                if values[x] > criterion_dict[colors[x]]:
                    valid = False
                    break

        if valid == True:
            id_numbers.append(int(game_id))

    return id_numbers

numbers = find_valid_games()
solution = sum(numbers)
print(solution)
# Solution:
#  2512
#  