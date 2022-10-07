# -----------------------------------------------------------------------------------
# --- Part Two ---
# Time to check the rest of the slopes - you need to minimize the probability
# of a sudden arboreal stop, after all.
#
# Determine the number of trees you would encounter if, for each of the 
# following slopes, you start at the top-left corner and traverse the map all
# the way to the bottom:
#
# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
#
# In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) 
# respectively; multiplied together, these produce the answer 336.
#
# What do you get if you multiply together the number of trees encountered on 
# each of the listed slopes?
# -----------------------------------------------------------------------------------

forest_array = []
with open('input.txt') as forest:
    for line in forest:
        forest_array.append(line)

i = 0
horr_num = 0
horr_slope = [1, 3, 5, 7, 1]
vert_slope = [1, 1, 1, 1, 2]
slope = 0
hit_tree = 0
total_mult = 1

while slope < len(horr_slope):
  i = vert_slope[slope]
  horr_num = horr_slope[slope]

  while i < len(forest_array):
  
    curr_line = list(forest_array[i])

    if curr_line[horr_num] == "#":
      hit_tree = hit_tree + 1

    i = i + vert_slope[slope]

    horr_num = horr_num + horr_slope[slope]
    while horr_num > 30:
      horr_num = horr_num - 31

  total_mult = total_mult * hit_tree
  hit_tree = 0
  slope = slope + 1

print(total_mult)
