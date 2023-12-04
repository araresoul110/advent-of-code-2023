from prep_input import *

def find_numbers(part):
    calibration_numbers = []

    raw_lines = prep_input('day1_input.txt')
    if (part == 2):
        Lines = replace_numbers(raw_lines)

    for line in Lines:
        first_number = 0
        second_number = 0

        for character in line:
            if character.isdigit():
                first_number = character
                break
        
        for character in "".join(reversed(line)):
            if character.isdigit():
                second_number = character
                break
        calibration_numbers.append(int(first_number + second_number))

    return calibration_numbers

def replace_numbers(Lines):
    new_lines = []
    
    for line in Lines:
        new_line = line.replace("one", "o1e").replace("two", "t2o").replace("three", "t3e").replace("four", "f4r").replace("five", "f5e").replace("six", "s6x").replace("seven", "s7n").replace("eight", "e8t").replace("nine", "n9e")
        newest_line = new_line.replace("o1e", "1").replace("t2o", "2").replace("t3e", "3").replace("f4r", "4").replace("f5e", "5").replace("s6x", "6").replace("s7n", "7").replace("e8t", "8").replace("n9e", "9")
        new_lines.append(newest_line)

    return new_lines

numbers = find_numbers(2)
solution = sum(numbers)
print(solution)
# Solution:
#  55488
#  55614