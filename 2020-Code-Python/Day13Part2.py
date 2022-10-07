# -----------------------------------------------------------------------------------
# --- Part Two ---
# The shuttle company is running a contest: one gold coin for anyone that can
# find the earliest timestamp such that the first bus ID departs at that time 
# and each subsequent listed bus ID departs at that subsequent minute. (The 
# first line in your input is no longer relevant.)
#
# For example, suppose you have the same list of bus IDs as above:
#
#     7,13,x,x,59,x,31,19
#
# An x in the schedule means there are no constraints on what bus IDs must 
# depart at that time.
#
# This means you are looking for the earliest timestamp (called t) such that:
#
#   - Bus ID 7 departs at timestamp t.
#   - Bus ID 13 departs one minute after timestamp t.
#   - There are no requirements or restrictions on departures at two or 
#     three minutes after timestamp t.
#   - Bus ID 59 departs four minutes after timestamp t.
#   - There are no requirements or restrictions on departures at five 
#     minutes after timestamp t.
#   - Bus ID 31 departs six minutes after timestamp t.
#   - Bus ID 19 departs seven minutes after timestamp t.
#
# The only bus departures that matter are the listed bus IDs at their 
# specific offsets from t. Those bus IDs can depart at other times, and other
# bus IDs can depart at those times. For example, in the list above, because 
# bus ID 19 must depart seven minutes after the timestamp at which bus ID 7 
# departs, bus ID 7 will always also be departing with bus ID 19 at seven 
# minutes after timestamp t.
#
# In this example, the earliest timestamp at which this occurs is 1068781:
# 
#     time     bus 7   bus 13  bus 59  bus 31  bus 19
#     1068773    .       .       .       .       .
#     1068774    D       .       .       .       .
#     1068775    .       .       .       .       .
#     1068776    .       .       .       .       .
#     1068777    .       .       .       .       .
#     1068778    .       .       .       .       .
#     1068779    .       .       .       .       .
#     1068780    .       .       .       .       .
#     1068781    D       .       .       .       .
#     1068782    .       D       .       .       .
#     1068783    .       .       .       .       .
#     1068784    .       .       .       .       .
#     1068785    .       .       D       .       .
#     1068786    .       .       .       .       .
#     1068787    .       .       .       D       .
#     1068788    D       .       .       .       D
#     1068789    .       .       .       .       .
#     1068790    .       .       .       .       .
#     1068791    .       .       .       .       .
#     1068792    .       .       .       .       .
#     1068793    .       .       .       .       .
#     1068794    .       .       .       .       .
#     1068795    D       D       .       .       .
#     1068796    .       .       .       .       .
#     1068797    .       .       .       .       .
#
# In the above example, bus ID 7 departs at timestamp 1068788 (seven minutes 
# after t). This is fine; the only requirement on that minute is that bus ID 
# 19 departs then, and it does.
#
# Here are some other examples:
#
#   - The earliest timestamp that matches the list 17,x,13,19 is 3417.
#   - 67,7,59,61 first occurs at timestamp 754018.
#   - 67,x,7,59,61 first occurs at timestamp 779210.
#   - 67,7,x,59,61 first occurs at timestamp 1261476.
#   - 1789,37,47,1889 first occurs at timestamp 1202161486.
#
# However, with so many bus IDs in your list, surely the actual earliest 
# timestamp will be larger than 100000000000000!
#
# What is the earliest timestamp such that all of the listed bus IDs depart
# at offsets matching their positions in the list?
# -----------------------------------------------------------------------------------

import re

input_array = []
my_file = open('input.txt')
content = my_file.read()

input_array = content.split("\n")

abus_array = re.split(",", input_array[1])
atime_array = []
time_array = []
bus_array = []

k = 0
while k < len(abus_array):
  atime_array.append(k)
  k = k + 1

k = 0
while k < len(abus_array):
  if abus_array[k] != "x":
    time_array.append(atime_array[k])
    bus_array.append(int(abus_array[k]))
  k = k + 1

print(time_array)
print(bus_array)

while "x" in bus_array:
  bus_array.remove("x")

print(time_array)
print(bus_array)

i = 1
increment = 1
base_it = 0
while i < len(bus_array):
  iteration = 0
  first_it = 0
  second_it = 0
  base_time = bus_array[0] * base_it
  it_time = 0
  print(time_array[i])
  print(bus_array[i])
  while ((it_time + time_array[i]) % bus_array[i] != 0):
    iteration = iteration + 1
    it_time = base_time + (bus_array[0] * increment * iteration)
    print(it_time)
  
  if i < (len(bus_array) - 1):
    first_it = iteration
    if i > 1:
      base_it = base_it + (increment * first_it)
    else:
      base_it = first_it
    iteration = iteration + 1
    it_time = it_time + (bus_array[0] * iteration)
  
    while ((it_time + time_array[i]) % bus_array[i] != 0):
      iteration = iteration + 1
      it_time = base_time + (bus_array[0] * increment * iteration)
    second_it = iteration
  
  print(it_time)
  print(increment)
  print(base_it)
  increment = increment * (second_it - first_it)
  print(increment)
  i = i + 1

print(it_time)
