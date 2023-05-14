test = False
if test:
    data_file = 'data/day1/input_test'
else:
    data_file = 'data/day1/input'

with open(data_file, 'r') as input_data:
    entries = input_data.read().splitlines()

entries = [int(line) for line in entries]


# quick function to sum elements in sliding window
def sum_of_window(arr, start, window_size):
    return sum(arr[start:start + window_size])


# initialize count at zero
count = 0

# part 2 variables
window_size = 3
count_p2 = 0

# part 1
# compare previous element to previous element starting at 1
for i in range(1, len(entries)):
    if entries[i] > entries[i - 1]:
        count += 1

# part 2
# iterates through entries comparing sums of each consecutive windows

for i in range(len(entries) - window_size):
    window_a_sum = sum_of_window(entries, i, window_size)
    window_b_sum = sum_of_window(entries, i + 1, window_size)

    if window_b_sum > window_a_sum:
        count_p2 += 1

print("number of times an increase happened for Part 1:", count)
print("number of times an increase happened for Part 2:", count_p2)
