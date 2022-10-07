# -----------------------------------------------------------------------------------
# --- Part Two ---
# Now that you've identified which tickets contain invalid values, discard 
# those tickets entirely. Use the remaining valid tickets to determine which
# field is which.
#
# Using the valid ranges for each field, determine what order the fields 
# appear on the tickets. The order is consistent between all tickets: if seat 
# is the third field, it is the third field on every ticket, including your 
# ticket.
#
# For example, suppose you have the following notes:
#
#     class: 0-1 or 4-19
#     row: 0-5 or 8-19
#     seat: 0-13 or 16-19
#
#     your ticket:
#     11,12,13
#
#     nearby tickets:
#     3,9,18
#     15,1,5
#     5,14,9
#
# Based on the nearby tickets in the above example, the first position must
# be row, the second position must be class, and the third position must be
# seat; you can conclude that in your ticket, class is 12, row is 11, and 
# seat is 13.
#
# Once you work out which field is which, look for the six fields on your 
# ticket that start with the word departure. What do you get if you multiply 
# those six values together?
# -----------------------------------------------------------------------------------

import re
import copy

input_array = []
my_file = open('input.txt')
content = my_file.read()

input_array = re.split("\n\n", content)

rules_array = input_array[0].split("\n")
my_ticket = input_array[1].split("\n")
my_ticket.pop(0)
tickets_array = input_array[2].split("\n")
tickets_array.pop(0)

i = 0
limits = []
while i < len(rules_array):
  curr_rule = re.split(": |-| or ", rules_array[i])
  limits.append([int(curr_rule[1]), int(curr_rule[2])])
  limits.append([int(curr_rule[3]), int(curr_rule[4])])
  i = i + 1

j = 0
while j < len(tickets_array):
  curr_ticket = tickets_array[j].split(",")
  k = 0
  while k < len(curr_ticket):
    l = 0
    while l < len(limits):
      bad = True
      if ((int(curr_ticket[k]) >= limits[l][0]) and (int(curr_ticket[k]) <= limits[l][1])) or ((int(curr_ticket[k]) >= limits[l + 1][0]) and (int(curr_ticket[k]) <= limits[l + 1][1])):
        bad = False
        l = len(limits)
      l = l + 2
    
    if bad == True:
      l = len(limits)
      k = len(curr_ticket)
    else:
      k = k + 1
  if bad == True:
    tickets_array.pop(j)
  else:
    j = j + 1

check_array = []
temp_array = []

m = 0
n = 0
while m < len(rules_array):
  n = 0
  temp_array.clear()
  while n < len(tickets_array):
    curr_ticket = tickets_array[n].split(",")
    temp_array.append(curr_ticket[m])
    n = n + 1
  check_array.append(copy.deepcopy(temp_array))
  m = m + 1

rule_found = False
comp_list = []
poss_rule = []
p = 0
while p < len(check_array):
  q = 0
  poss_rule.clear()
  while q < len(rules_array):
    curr_rule = re.split(": |-| or ", rules_array[q])
    r = 0
    while r < len(check_array[p]):
      if (int(check_array[p][r]) >= int(curr_rule[1]) and int(check_array[p][r]) <= int(curr_rule[2])) or (int(check_array[p][r]) >= int(curr_rule[3]) and int(check_array[p][r]) <= int(curr_rule[4])):
        rule_found = True
        r = r + 1
      else:
        rule_found = False
        r = len(check_array[p])
    
    if rule_found == True:
      poss_rule.append(curr_rule[0])
    q = q + 1
  comp_list.append(copy.deepcopy(poss_rule))
  p = p + 1

w = 0
rule_list = []
while w < len(comp_list):
  rule_list.append([])
  w = w + 1
t = 0
while t < len(comp_list):
  u = 0
  while u < len(comp_list):
    if len(comp_list[u]) == 1:
      rule_list[u].append(copy.deepcopy(comp_list[u][0]))
      t = t + 1
      v = 0
      while v < len(comp_list):
        if rule_list[u][0] in comp_list[v]:
          comp_list[v].remove(rule_list[u][0])
        v = v + 1
    u = u + 1

print(rule_list)

my_ticket_array = my_ticket[0].split(",")
value = 1
x = 0
while x < len(my_ticket_array):
  if rule_list[x][0].startswith("departure"):
    value = value * int(my_ticket_array[x])
  x = x + 1
  
print(value)
