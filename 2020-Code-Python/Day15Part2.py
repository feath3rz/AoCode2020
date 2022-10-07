# -----------------------------------------------------------------------------------
# --- Part Two ---
# Impressed, the Elves issue you a challenge: determine the 30000000th number 
# spoken. For example, given the same starting numbers as above:
#
#   - Given 0,3,6, the 30000000th number spoken is 175594.
#   - Given 1,3,2, the 30000000th number spoken is 2578.
#   - Given 2,1,3, the 30000000th number spoken is 3544142.
#   - Given 1,2,3, the 30000000th number spoken is 261214.
#   - Given 2,3,1, the 30000000th number spoken is 6895259.
#   - Given 3,2,1, the 30000000th number spoken is 18.
#   - Given 3,1,2, the 30000000th number spoken is 362.
#
# Given your starting numbers, what will be the 30000000th number spoken?
# -----------------------------------------------------------------------------------
# NOTE: I think this took a while to get the answer, it doesn't seem to run
# well so I'm unsure if the answer comes out correctly.
# -----------------------------------------------------------------------------------

import re

input_array = []
my_file = open('input.txt')
content = my_file.read()

input_array = re.split(",", content)

count_array = []
num_array = []


j = 0
while j < len(input_array):
  num_array.append(int(input_array[j]))
  count_array.append([j])
  j = j + 1
print(num_array)
print(count_array)

count_array[0].append(j)
i = j + 1
last_spoken = 0
spoken = 0
while i < 30000000:
  last_spoken = spoken
  if i % 10000 == 0:
    print(i)
  num_loc = num_array.index(last_spoken)
  if len(count_array[num_loc]) == 2:
    spoken = count_array[num_loc][1] - count_array[num_loc][0]
  else:
    spoken = 0

  if spoken in num_array:
    num_loc = num_array.index(spoken)
    if len(count_array[num_loc]) == 2:
      count_array[num_loc].pop(0)
  else:
    num_array.append(spoken)
    count_array.append([])
    num_loc = len(num_array) - 1

  count_array[num_loc].append(i)
  i = i + 1

print(spoken)
