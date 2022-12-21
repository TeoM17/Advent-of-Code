input = open("input.txt", "r")
score = 0
test = {"BX": 1, "CY": 2, "AZ": 3, "AX":4, "BY": 5, "CZ": 6, "CX": 7, "AY": 8, "BZ": 9}
val = ""
input_string = input.read()
for char in input_string:
    if char != ' ' and char != '\n':
        val += char
    elif char == '\n':
        score += test.get(val, 0)
        val = ""
print(score)