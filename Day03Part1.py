# https://adventofcode.com/2020/day/3

# --- Day 3: Toboggan Trajectory ---
# With the toboggan login problems resolved, you set off toward the airport. 
# While travel by toboggan might be easy, it's certainly not safe: there's 
# very minimal steering and the area is covered in trees. You'll need to see
# which angles will take you near the fewest trees.

# Due to the local geology, trees in this area only grow on exact integer 
# coordinates in a grid. You make a map (your puzzle input) of the open 
# squares (.) and trees (#) you can see. For example:

#   ..##.......
#   #...#...#..
#   .#....#..#.
#   ..#.#...#.#
#   .#...##..#.
#   ..#.##.....
#   .#.#.#....#
#   .#........#
#   #.##...#...
#   #...##....#
#   .#..#...#.#

# These aren't the only trees, though; due to something you read about once 
# involving arboreal genetics and biome stability, the same pattern repeats
# to the right many times:

#   ..##.........##.........##.........##.........##.........##.......  --->
#   #...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
#   .#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
#   ..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
#   .#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
#   ..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
#   .#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
#   .#........#.#........#.#........#.#........#.#........#.#........#
#   #.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#   #...##....##...##....##...##....##...##....##...##....##...##....#
#   .#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

# You start on the open square (.) in the top-left corner and need to reach 
# the bottom (below the bottom-most row on your map).

# The toboggan can only follow a few specific slopes (you opted for a cheaper 
# model that prefers rational numbers); start by counting all the trees you 
# would encounter for the slope right 3, down 1:

# From your starting position at the top-left, check the position that is 
# right 3 and down 1. Then, check the position that is right 3 and down 1 
# from there, and so on until you go past the bottom of the map.

# The locations you'd check in the above example are marked here with O where 
# there was an open square and X where there was a tree:

#   ..##.........##.........##.........##.........##.........##.......  --->
#   #..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
#   .#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
#   ..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
#   .#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
#   ..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
#   .#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
#   .#........#.#........X.#........#.#........#.#........#.#........#
#   #.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#   #...##....##...##....##...#X....##...##....##...##....##...##....#
#   .#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

# In this example, traversing the map using this slope would cause you to 
# encounter 7 trees.

# Starting at the top-left corner of your map and following a slope of right 
# 3 and down 1, how many trees would you encounter?

forest_array = []
with open('input.txt') as forest:
    for line in forest:
        forest_array.append(line)

i = 1
horr_num = 3
hit_tree = 0

while i < len(forest_array):
  
  curr_line = list(forest_array[i])

  if curr_line[horr_num] == "#":
    hit_tree = hit_tree + 1

  i = i + 1

  horr_num = horr_num + 3
  while horr_num > 30:
    horr_num = horr_num - 31

print(hit_tree)