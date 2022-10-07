# -----------------------------------------------------------------------------------
# https://adventofcode.com/2020/day/1
#
# --- Day 1: Report Repair ---
# After saving Christmas five years in a row, you've decided to take a
# vacation at a nice resort on a tropical island. Surely, Christmas will go
# on without you.
#
# The tropical island has its own currency and is entirely cash-only. The
# gold coins used there have a little picture of a starfish; the locals just
# call them stars. None of the currency exchanges seem to have heard of them,
# but somehow, you'll need to find fifty of these coins by the time you
# arrive so you can pay the deposit on your room.
#
# To save your vacation, you need to get all fifty stars by December 25th.
#
# Collect stars by solving puzzles. Two puzzles will be made available on 
# each day in the Advent calendar; the second puzzle is unlocked when you 
# complete the first. Each puzzle grants one star. Good luck!
#
# Before you leave, the Elves in accounting just need you to fix your expense 
# report (your puzzle input); apparently, something isn't quite adding up.
#
# Specifically, they need you to find the two entries that sum to 2020 and 
# then multiply those two numbers together.
#
# For example, suppose your expense report contained the following:
#
#     1721
#     979
#     366
#     299
#     675
#     1456
#
# In this list, the two entries that sum to 2020 are 1721 and 299.
# Multiplying them together produces 1721 * 299 = 514579, so the correct 
# answer is 514579.
#
# Of course, your expense report is much larger. Find the two entries that 
# sum to 2020; what do you get if you multiply them together?
# -----------------------------------------------------------------------------------

entry_array = []
with open('data.txt') as amounts:
    for line in amounts:
        entry_array.append(int(line))

my_position = 0
check_this = 0
checking_position = 0;
num1 = 0;
num2 = 0;

while my_position < len(entry_array):
  check_this = 2020 - entry_array[my_position]
  checking_position = my_position + 1

  while checking_position < len(entry_array):
    if check_this == entry_array[checking_position]:
      num1 = entry_array[my_position]
      num2 = check_this
      checking_position = len(entry_array)
      my_position = len(entry_array)
    else:
      checking_position = checking_position + 1
  my_position = my_position + 1

print (num1 * num2)
