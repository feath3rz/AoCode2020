# -----------------------------------------------------------------------------------
# --- Part Two ---
# For some reason, the sea port's computer system still can't communicate 
# with your ferry's docking program. It must be using version 2 of the 
# decoder chip!
#
# A version 2 decoder chip doesn't modify the values being written at all. 
# Instead, it acts as a memory address decoder. Immediately before a value is 
# written to memory, each bit in the bitmask modifies the corresponding bit 
# of the destination memory address in the following way:
#
#   - If the bitmask bit is 0, the corresponding memory address bit is 
#     unchanged.
#   - If the bitmask bit is 1, the corresponding memory address bit is
#     overwritten with 1.
#   - If the bitmask bit is X, the corresponding memory address bit is 
#     floating.
#
# A floating bit is not connected to anything and instead fluctuates
# unpredictably. In practice, this means the floating bits will take on all 
# possible values, potentially causing many memory addresses to be written
# all at once!
#
# For example, consider the following program:
# 
#     mask = 000000000000000000000000000000X1001X
#     mem[42] = 100
#     mask = 00000000000000000000000000000000X0XX
#     mem[26] = 1
#
# When this program goes to write to memory address 42, it first applies the 
# bitmask:
#
#     address: 000000000000000000000000000000101010  (decimal 42)
#     mask:    000000000000000000000000000000X1001X
#     result:  000000000000000000000000000000X1101X
#
# After applying the mask, four bits are overwritten, three of which are 
# different, and two of which are floating. Floating bits take on every
# possible combination of values; with two floating bits, four actual memory 
# addresses are written:
#
#     000000000000000000000000000000011010  (decimal 26)
#     000000000000000000000000000000011011  (decimal 27)
#     000000000000000000000000000000111010  (decimal 58)
#     000000000000000000000000000000111011  (decimal 59)
#
# Next, the program is about to write to memory address 26 with a different
# bitmask:
#
#     address: 000000000000000000000000000000011010  (decimal 26)
#     mask:    00000000000000000000000000000000X0XX
#     result:  00000000000000000000000000000001X0XX
#
# This results in an address with three floating bits, causing writes to
# eight memory addresses:
#
#     000000000000000000000000000000010000  (decimal 16)
#     000000000000000000000000000000010001  (decimal 17)
#     000000000000000000000000000000010010  (decimal 18)
#     000000000000000000000000000000010011  (decimal 19)
#     000000000000000000000000000000011000  (decimal 24)
#     000000000000000000000000000000011001  (decimal 25)
#     000000000000000000000000000000011010  (decimal 26)
#     000000000000000000000000000000011011  (decimal 27)
#
# The entire 36-bit address space still begins initialized to the value 0 at 
# every address, and you still need the sum of all values left in memory at 
# the end of the program. In this example, the sum is 208.
#
# Execute the initialization program using an emulator for a version 2 
# decoder chip. What is the sum of all values left in memory after it 
# completes?
# -----------------------------------------------------------------------------------

import re

input_array = []
my_file = open('input.txt')
content = my_file.read()

input_array = content.split("\n")

memory_array = []
answer_array = []
value_array = []

def possible(the_data, the_loc, da_value):
  m = 0
  da_total = 0
  #print(the_loc)
  temp_loc = the_loc[m]
  temp_len = len(the_loc)
  #print(temp_len)
  while m < 2:
    if m == 0:
      the_data[temp_loc] = 0
    elif m == 1:
      the_data[temp_loc] = 1
      
    temp_poss = [0]*36

    if temp_len > 1 and (m == 0 or m == 1):
      da_total = da_total + possible(the_data, the_loc[1:], da_value)
      #print(da_total)
    else:
      n = 0
      while n < len(the_data):
        temp_poss[n] = str(the_data[n])
        n = n + 1
      sample = int("".join(temp_poss), base=2)
      if sample not in answer_array:
        answer_array.append(sample)
        value_array.append(da_value)
      else:
        value_array[answer_array.index(sample)] = da_value
    m = m + 1
  return da_total

i = 0
in_array = 0
total = 0

while i < len(input_array):
  curr_select = re.split("mask = |mem\[|\] = ", input_array[i])
  curr_select.remove("")
  #print(curr_select)
  if len(curr_select) == 1:
    curr_mask = list(curr_select[0])
    l = 0
    while l < len(curr_mask):
      if curr_mask[l] != "X":
        curr_mask[l] = int(curr_mask[l])
      l = l + 1
  else:
    mem_loc = int(curr_select[0])
    value = int(curr_select[1])

    temp_data = format(mem_loc, "036b")
    bin_data = list(temp_data)
    temp_bin = [0]*36

    k = 0
    while k < len(bin_data):
      if curr_mask[k] == "X":
        temp_bin[k] = curr_mask[k]
      elif curr_mask[k] == 1:
        temp_bin[k] = curr_mask[k]
      else:
        temp_bin[k] = bin_data[k]
      k = k + 1

    loc_x = []
    j = 0
    while j < len(temp_bin):
      if temp_bin[j] == "X":
        loc_x.append(j)
      j = j + 1
    total = total + possible(temp_bin, loc_x, value)
  i = i + 1

q = 0
total = 0
print(answer_array)
print(value_array)
while q < len(value_array):
  total = total + value_array[q]
  q = q + 1

print(total)
