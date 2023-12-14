from prep_input import *

def start_search(part):
    Lines = prep_input('day3_input.txt')
    if part == 1:
        final_numbers = find_part_numbers(Lines)
    else:
        final_numbers = find_gear_ratios(Lines)
    return final_numbers

def find_part_numbers(Lines):
    numbers = []
    special_symbols = ["@", "#", "$", "%", "&", "*", "/", "-", "=", "+"]

    for line_number, line in enumerate(Lines):
        index = 0
        while index < len(line):
            if line[index].isdigit():
                start_index = index
                end_index = min(start_index + 1, len(line))
                x = 1
                while line[start_index + x].isdigit():
                    end_index += 1
                    x += 1 
                    if start_index + x >= len(line):
                        break
                
                square = []
                for x in range(-1, 2):
                    if line_number + x >= 0 and line_number + x < len(Lines):
                        square.append(Lines[line_number + x][(max(start_index - 1,0)):(end_index + 1)])

                for element in square:
                    for this_char in element:
                        if this_char in special_symbols:
                            numbers.append(int(Lines[line_number][start_index:end_index]))
                            break

                index = end_index
            index += 1
    return numbers

def find_gear_ratios(Lines):
    numbers = []

    for line_number, line in enumerate(Lines):
        index = 0
        while index < len(line):
            if line[index] == '*':
                square = []
                for x in range(-1, 2):
                    if line_number == 0 or line_number == len(Lines) - 1:
                        x += 1
                    square.append(fill_square_section(Lines, line_number + x, max(index - 1,0), min(index + 1, len(line))))
                
                square_string = (square[0] + "." + square[1] + "." + square[2]).replace("*", ".")
                values = [int(i) for i in square_string.split(".") if i.isdigit()]
                test = values
                if len(values) == 2:
                    numbers.append(values[0] * values[1])

                index = min(index + 1, len(line))
            index += 1
    return numbers

def fill_square_section(Lines, line_number, start_index, end_index):
    square = Lines[line_number][start_index:(end_index + 1)]

    if square[0].isdigit():
        x = 1
        while start_index - x >= 0 and Lines[line_number][start_index - x].isdigit():
            square = Lines[line_number][start_index - x] + square
            x += 1
    
    if square[-1].isdigit():
        x = 1
        while end_index + x < len(Lines[line_number]) and Lines[line_number][end_index + x].isdigit():
            square = square + Lines[line_number][end_index + x]
            x += 1

    return square

numbers = start_search(2)
solution = sum(numbers)

print(solution)
# Solution:
#  532331
#  82301120