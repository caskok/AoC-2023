lines = open('input/input1.txt', 'r').readlines()
D = [line.strip() for line in lines]
p1 = 0
p2 = 0
for line in D:
    p1_digits = []
    p2_digits = []
    for i, character in enumerate(line):
        if character.isdigit():
            p1_digits.append(character)
            p2_digits.append(character)
        for digit, number_string in enumerate(['one', 'two', 'three',
                                               'four', 'five', 'six',
                                               'seven', 'eight', 'nine']):
            if line[i:].startswith(number_string):
                p2_digits.append(str(digit + 1))
    p1 += int(p1_digits[0] + p1_digits[-1])
    p2 += int(p2_digits[0] + p2_digits[-1])
print(p1)
print(p2)
