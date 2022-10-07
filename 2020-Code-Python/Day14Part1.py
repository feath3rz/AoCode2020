# -----------------------------------------------------------------------------------
# https://adventofcode.com/2020/day/14
#
# --- Day 14: Docking Data ---
# As your ferry approaches the sea port, the captain asks for your help 
# again. The computer system that runs this port isn't compatible with the 
# docking program on the ferry, so the docking parameters aren't being 
# correctly initialized in the docking program's memory.
# 
# After a brief inspection, you discover that the sea port's computer system 
# uses a strange bitmask system in its initialization program. Although you
# don't have the correct decoder chip handy, you can emulate it in software!
#
# The initialization program (your puzzle input) can either update the 
# bitmask or write a value to memory. Values and memory addresses are both 
# 36-bit unsigned integers. For example, ignoring bitmasks for a moment, a 
# line like mem[8] = 11 would write the value 11 to memory address 8.
#
# The bitmask is always given as a string of 36 bits, written with the most
# significant bit (representing 2^35) on the left and the least significant 
# bit (2^0, that is, the 1s bit) on the right. The current bitmask is applied
# to values immediately before they are written to memory: a 0 or 1 
# overwrites the corresponding bit in the value, while an X leaves the bit in
# the value unchanged.
#
# For example, consider the following program:
#
#     mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
#     mem[8] = 11
#     mem[7] = 101
#     mem[8] = 0
#
# This program starts by specifying a bitmask (mask = ....). The mask it 
# specifies will overwrite two bits in every written value: the 2s bit is
# overwritten with 0, and the 64s bit is overwritten with 1.
#
# The program then attempts to write the value 11 to memory address 8. By 
# expanding everything out to individual bits, the mask is applied as 
# follows:
#
#     value:  000000000000000000000000000000001011  (decimal 11)
#     mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
#     result: 000000000000000000000000000001001001  (decimal 73)
#
# So, because of the mask, the value 73 is written to memory address 8 
# instead. Then, the program tries to write 101 to address 7:
#
#     value:  000000000000000000000000000001100101  (decimal 101)
#     mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
#     result: 000000000000000000000000000001100101  (decimal 101)
#
# This time, the mask has no effect, as the bits it overwrote were already 
# the values the mask tried to set. Finally, the program tries to write 0 to
# address 8:
#
#     value:  000000000000000000000000000000000000  (decimal 0)
#     mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
#     result: 000000000000000000000000000001000000  (decimal 64)
#
# 64 is written to address 8 instead, overwriting the value that was there
# previously.
#
# To initialize your ferry's docking program, you need the sum of all values
# left in memory after the initialization program completes. (The entire 36-
# bit address space begins initialized to the value 0 at every address.) In 
# the above example, only two values in memory are not zero - 101 (at address
# 7) and 64 (at address 8) - producing a sum of 165.
# 
# Execute the initialization program. What is the sum of all values left in 
# memory after it completes? (Do not truncate the sum to 36 bits.)
# -----------------------------------------------------------------------------------

import re

input_array = []
my_file = open('input.txt')
content = my_file.read()

input_array = content.split("\n")

memory_array = []

i = 0
in_array = 0

while i < len(input_array):
  curr_select = re.split("mask = |mem\[|\] = ", input_array[i])
  curr_select.remove("")
  print(curr_select)
  if len(curr_select) == 1:
    curr_mask = list(curr_select[0])
    l = 0
    while l < len(curr_mask):
      if curr_mask[l] != "X":
        curr_mask[l] = int(curr_mask[l])
      l = l + 1
  else:
    mem_loc = int(curr_select[0])
    mem_data = int(curr_select[1])

    j = 0
    mem_exists = False
    while j <= len(memory_array):
      if len(memory_array) == 0:
        memory_array.append([mem_loc])
        in_array = 0
        j = len(memory_array) + 1
      elif j == len(memory_array):
        memory_array.append([mem_loc])
        in_array = len(memory_array) - 1
        j = len(memory_array) + 1
      elif (j < len(memory_array)) and (memory_array[j][0] == mem_loc):
        mem_exists = True
        in_array = j
        j = len(memory_array) + 1
      j = j + 1
    bin_array = [0]*36
    temp_data = format(mem_data, "036b")
    bin_data = list(temp_data)

    k = 0
    if mem_exists == False:
      while k < len(bin_data):
        if curr_mask[k] == "X":
          memory_array[in_array].append(bin_data[k])
        else:
          memory_array[in_array].append(curr_mask[k])
        k = k + 1
    else:
      while k < len(bin_data):
        if curr_mask[k] == "X":
          memory_array[in_array][k + 1] = bin_data[k]
        else:
          memory_array[in_array][k + 1] = curr_mask[k]
        k = k + 1

  print(curr_mask)
  i = i + 1

total = 0
m = 0
while m < len(memory_array):
  print(memory_array[m])
  n = 1
  while n < len(memory_array[m]):
    memory_array[m][n] = str(memory_array[m][n])
    n = n + 1
  curr_value = int("".join(memory_array[m][1:]), base=2)
  total = total + curr_value
  print("here:", curr_value)
  m = m + 1

print(total)
