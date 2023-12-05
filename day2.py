from prep_input import *

def process_games(part):
    numbers = []
    Lines = prep_input('day2_input.txt')

    for line in Lines:
        game_id = line[:line.index(":")].replace("Game", "")
        split_line = line.replace(":", ";").split(";")
        if part == 1:
            if find_valid_games(split_line):
                numbers.append(int(game_id))
        else:
            numbers.append(find_minimum_cubes(split_line))
    
    return numbers
        

def find_valid_games(split_line):
    criterion_dict ={"red": 12, "green": 13, "blue": 14}

    valid = True
    for handful in split_line[1:]:
        values = [int(i) for i in handful.split() if i.isdigit()]
        colors = [j.replace(",", "") for j in handful.split() if j.isdigit() == False]
        for x in range(len(colors)):
            if values[x] > criterion_dict[colors[x]]:
                valid = False
                break

    return valid

def find_minimum_cubes(split_line):
    minimum_dict ={"red": 0, "green": 0, "blue": 0}
    for handful in split_line[1:]:
        values = [int(i) for i in handful.split() if i.isdigit()]
        colors = [j.replace(",", "") for j in handful.split() if j.isdigit() == False]
        for x in range(len(colors)):
            if values[x] > minimum_dict[colors[x]]:
                minimum_dict[colors[x]] = values[x]
    return minimum_dict["red"] * minimum_dict["blue"] * minimum_dict["green"]

numbers = process_games(2)
solution = sum(numbers)

print(solution)
# Solution:
#  2512
#  