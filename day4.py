from prep_input import *

def analyze_cards(part):
    total_score = 0
    win_count_per_card = []
    Lines = prep_input('day4_input.txt')
    
    for line in Lines:
        winning_numbers = line[line.index(":") + 1:line.index("|")].split()
        assigned_numbers = line[line.index("|") + 1:].split()
        win_count_per_card.append(len([i for i in assigned_numbers if i in winning_numbers]))

        if part == 1:
            total_score += score_card(win_count_per_card)

    if part == 2:
        total_score = count_cards_won(win_count_per_card)

    return total_score

def score_card(win_count_per_card):
    score = 0

    if win_count_per_card[-1] > 0:
        score = 1
        for x in range(win_count_per_card[-1] - 1):
            score *= 2

    return score

def count_cards_won(win_count_per_card):
    num_instances_won = [1 for i in range(len(win_count_per_card))]

    for i, card in enumerate(win_count_per_card):
        if card > 0:
            for x in range(card):
                num_instances_won[i + x + 1] += num_instances_won[i]

    return sum(num_instances_won)

solution = analyze_cards(2)

print(solution)
# Solution:
#  28750
#  1230