test = False
if test:
    data_file = 'data/day2/input_test'
else:
    data_file = 'data/day2/input'

with open(data_file, 'r') as input_data:
    entries = input_data.read().splitlines()

# split each line into a command and value, and convert second value to int
entries = [[line.split()[0], int(line.split()[1])] for line in entries]

depth = 0
horizontal = 0
# part 2
aim = 0

for i in range(0, len(entries)):
    if entries[i][0] == "forward":
        horizontal += entries[i][1]
        depth += aim * entries[i][1]
    elif entries[i][0] == "down":
        aim += entries[i][1]
    else:
        aim -= entries[i][1]

final_value = depth * horizontal

print("The Depth Is:" + str(depth))
print("The Horizontal is:" + str(horizontal))
print("The Final Value is:" + str(final_value))