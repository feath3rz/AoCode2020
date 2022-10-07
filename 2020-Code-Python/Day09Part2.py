# -----------------------------------------------------------------------------------
# --- Part Two ---
# The final step in breaking the XMAS encryption relies on the invalid number 
# you just found: you must find a contiguous set of at least two numbers in 
# your list which sum to the invalid number from step 1.
#
# Again consider the above example:
#
#     35
#     20
#     15
#     25
#     47
#     40
#     62
#     55
#     65
#     95
#     102
#     117
#     150
#     182
#     127
#     219
#     299
#     277
#     309
#     576
#
# In this list, adding up all of the numbers from 15 through 40 produces the 
# invalid number from step 1, 127. (Of course, the contiguous set of numbers 
# in your actual list might be much longer.)
#
# To find the encryption weakness, add together the smallest and largest 
# number in this contiguous range; in this example, these are 15 and 47, 
# producing 62.
#
# What is the encryption weakness in your XMAS-encrypted list of numbers?
# -----------------------------------------------------------------------------------

preamble_array = []
my_file = open('input.txt')
content = my_file.read()

preamble_array = content.split("\n")
t = 0
while t < len(preamble_array):
  preamble_array[t] = int(preamble_array[t])
  t = t + 1 

pre_begin = 0
pre_end = 24
i = 25
error = False
Found = False

def add_it(the_start, the_end, solution):
  total = sum(preamble_array[the_start:the_end])
  #while the_start <= the_end:
    #total = total + preamble_array[the_start]
    #the_start = the_start + 1
    #if total > solution:
      #the_start = the_end + 1
  return total

while error == False:
  while i < len(preamble_array):
    move_start = pre_begin
    move_end = pre_begin + 1
    while move_start < pre_end:
      while move_end <= pre_end:
        if preamble_array[i] == preamble_array[move_start] + preamble_array[move_end]:
          Found = True
          move_end = pre_end + 1
          move_start = pre_end
        else:
          move_end = move_end + 1
      move_start = move_start + 1
      move_end = move_start + 1
    if Found == False:
      error = True
      print_me = preamble_array[i]
      i = len(preamble_array)
    else:
      i = i + 1
      pre_begin = pre_begin + 1
      pre_end = pre_end + 1
      Found = False

add_start = 0
add_end = add_start + 1
adding = 0
Found = False

while Found != True:
  while add_start < len(preamble_array):
    while add_end < len(preamble_array):
      adding = add_it(add_start, add_end, print_me)
      if adding == print_me:
        print("wtf you found it?")
        Found = True
        num1 = add_start
        num2 = add_end
        add_end = len(preamble_array)
        add_start = add_end
      elif adding > print_me:
        add_end = len(preamble_array)
      else:
        add_end = add_end + 1
    add_start = add_start + 1
    add_end = add_start + 1

answer1 = preamble_array[num1]
answer2 = preamble_array[num2]

while num1 <= num2:
  if answer1 > preamble_array[num1]:
    answer1 = preamble_array[num1]
  elif preamble_array[num1] > answer2:
    answer2 = preamble_array[num1]
  num1 = num1 + 1
  
print(answer1 + answer2)
