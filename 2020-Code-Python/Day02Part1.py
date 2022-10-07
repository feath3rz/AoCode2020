# -----------------------------------------------------------------------------------
# https://adventofcode.com/2020/day/2
#
# --- Day 2: Password Philosophy ---
# Your flight departs in a few days from the coastal airport; the easiest way
# down to the coast from here is via toboggan.
#
# The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day.
# "Something's wrong with our computers; we can't log in!" You ask if you can
# take a look.
#
# Their password database seems to be a little corrupted: some of the
# passwords wouldn't have been allowed by the Official Toboggan Corporate 
# Policy that was in effect when they were chosen.
#
# To try to debug the problem, they have created a list (your puzzle input) 
# of passwords (according to the corrupted database) and the corporate policy
# when that password was set.
#
# For example, suppose you have the following list:
#
#     1-3 a: abcde
#     1-3 b: cdefg
#     2-9 c: ccccccccc
#
# Each line gives the password policy and then the password. The password 
# policy indicates the lowest and highest number of times a given letter must
# appear for the password to be valid. For example, 1-3 a means that the 
# password must contain a at least 1 time and at most 3 times.
#
# In the above example, 2 passwords are valid. The middle password, cdefg, is 
# not; it contains no instances of b, but needs at least 1. The first and 
# third passwords are valid: they contain one a or nine c, both within the 
# limits of their respective policies.
#
# How many passwords are valid according to their policies?
# -----------------------------------------------------------------------------------

import re

entry_array = []
with open('input.txt') as amounts:
    for line in amounts:
        entry_array.append(line)

i = 0
passi = 0
count = 0
good_passwords = 0

while i < len(entry_array):
  sample = re.split('-| |: ',entry_array[i])
  minAmt = int(sample[0])
  maxAmt = int(sample[1])
  find_char = sample [2]

  password = list(sample[3])

  while passi < len(password):
    if password[passi] == find_char:
      count = count + 1
    passi = passi + 1

  
  if (count >= minAmt) and (count <= maxAmt):
    good_passwords = good_passwords + 1
  
  passi = 0
  count = 0
  i = i + 1

print(good_passwords)
