def prep_input(input_file):
    with open(input_file) as f:
        Lines = [line.rstrip('\n') for line in f]
    return Lines