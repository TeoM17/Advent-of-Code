import time
start_time = time.time()

file = open("file.txt", "r")
total = 0
largest_val = 0
cur_index = 1
output = []
for each_line in file.readlines():
    if each_line == '\n':
        output.append(total)
        total = 0
    else:
        total += int(each_line)
output.sort(reverse=True)
print(output[0]+output[1]+output[2])

# checking if program compiles quickly
print("Compiled in %s seconds" % (time.time() - start_time))