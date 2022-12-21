import time
start_time = time.time()

file = open("file.txt", "r")
total = 0
largest_val = 0
cur_index = 1
for each_line in file.readlines():
    if each_line == '\n':
        largest_val = max(total, largest_val)
        if largest_val == total:
            output = (largest_val, cur_index)
        total = 0
        cur_index += 1
    else:
        total += int(each_line)
print(output[0])

# checking if program compiles quickly
print("Compiled in %s seconds" % (time.time() - start_time))