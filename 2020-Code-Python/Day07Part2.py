# -----------------------------------------------------------------------------------
# --- Part Two ---
# It's getting pretty expensive to fly these days - not because of ticket 
# prices, but because of the ridiculous number of bags you need to buy!
#
# Consider again your shiny gold bag and the rules from the above example:
#
#   - faded blue bags contain 0 other bags.
#   - dotted black bags contain 0 other bags.
#   - vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 
#     dotted black bags.
#   - dark olive bags contain 7 other bags: 3 faded blue bags and 4 
#     dotted black bags.
#
# So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags
# within it) plus 2 vibrant plum bags (and the 11 bags within each of those):
# 1 + 1*7 + 2 + 2*11 = 32 bags!
#
# Of course, the actual rules have a small chance of going several levels 
# deeper than this example; be sure to count all of the bags, even if the 
# nesting becomes topologically impractical!
#
# Here's another example:
#
#     shiny gold bags contain 2 dark red bags.
#     dark red bags contain 2 dark orange bags.
#     dark orange bags contain 2 dark yellow bags.
#     dark yellow bags contain 2 dark green bags.
#     dark green bags contain 2 dark blue bags.
#     dark blue bags contain 2 dark violet bags.
#     dark violet bags contain no other bags.
#
# In this example, a single shiny gold bag must contain 126 other bags.
#
# How many individual bags are required inside your single shiny gold bag?
# -----------------------------------------------------------------------------------

import re

rules_array = []
my_file = open('input.txt')
content = my_file.read()

rules_array = content.split("\n")
check_this = "shiny gold bags"

def find_bag(thebag):
  move = 0
  inside = 0
  if (thebag == 'other bag'):
    return 1
  else: 
    while move < len(rules_array):
      if (rules_array[move].startswith(thebag)):
        current_rule = re.split(' contain |, |\.', rules_array[move])
        current_rule.remove("")
        bag_elem = 1
        while bag_elem < len(current_rule):
          curr_part = re.split(' ', current_rule[bag_elem])
          print(curr_part)
          next_bag = [' '.join(curr_part[1:4])]
          print(next_bag)
          if curr_part[0] == 'no':
            return 0
          else:
            inside = inside + int(curr_part[0]) + (int(curr_part[0]) * find_bag(next_bag[0]))
          bag_elem = bag_elem + 1
      move = move + 1
    return inside

print(find_bag(check_this))
