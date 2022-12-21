input = open("input.txt", "r")
score = 0
test = {"BX": 1, "CX": 2, "AX": 3, "AY": 4,  "BY": 5, "CY": 6, "CZ": 7, "AZ": 8, "BZ": 9}
val = ""
input_string = input.read()
for char in input_string:
    if char != ' ' and char != '\n':
        val += char
    elif char == '\n':
        score += test.get(val, 0)
        val = ""
print(score)