# -----------------------------------------------------------------------------------
# --- Day 17: Conway Cubes ---
# As your flight slowly drifts through the sky, the Elves at the Mythical 
# Information Bureau at the North Pole contact you. They'd like some help 
# debugging a malfunctioning experimental energy source aboard one of their 
# super-secret imaging satellites.
#
# The experimental energy source is based on cutting-edge technology: a set 
# of Conway Cubes contained in a pocket dimension! When you hear it's having 
# problems, you can't help but agree to take a look.
#
# The pocket dimension contains an infinite 3-dimensional grid. At every 
# integer 3-dimensional coordinate (x,y,z), there exists a single cube 
# which is either active or inactive.
#
# In the initial state of the pocket dimension, almost all cubes start 
# inactive. The only exception to this is a small flat region of cubes (your
# puzzle input); the cubes in this region start in the specified active (#) 
# or inactive (.) state.
#
# The energy source then proceeds to boot up by executing six cycles.
#
# Each cube only ever considers its neighbors: any of the 26 other cubes
# where any of their coordinates differ by at most 1. For example, given the
# cube at x=1,y=2,z=3, its neighbors include the cube at x=2,y=2,z=2, the 
# cube at x=0,y=2,z=3, and so on.
#
# During a cycle, all cubes simultaneously change their state according to
# the following rules:
#
#   - If a cube is active and exactly 2 or 3 of its neighbors are also
#     active, the cube remains active. Otherwise, the cube becomes inactive.
#   - If a cube is inactive but exactly 3 of its neighbors are active, the 
#     cube becomes active. Otherwise, the cube remains inactive.
#
# The engineers responsible for this experimental energy source would like 
# you to simulate the pocket dimension and determine what the configuration
# of cubes should be at the end of the six-cycle boot process.
#
# For example, consider the following initial state:
#
#     .#.
#     ..#
#     ###
# Even though the pocket dimension is 3-dimensional, this initial state 
# represents a small 2-dimensional slice of it. (In particular, this initial 
# state defines a 3x3x1 region of the 3-dimensional space.)
#
# Simulating a few cycles from this initial state produces the following 
# configurations, where the result of each cycle is shown layer-by-layer at
# each given z coordinate (and the frame of view follows the active cells in
# each cycle):
#
#     Before any cycles:
#
#     z=0
#     .#.
#     ..#
#     ###
#
#
#     After 1 cycle:
#
#     z=-1
#     #..
#     ..#
#     .#.
#
#     z=0
#     #.#
#     .##
#     .#.
#
#     z=1
#     #..
#     ..#
#     .#.
#
#
#     After 2 cycles:
#
#     z=-2
#     .....
#     .....
#     ..#..
#     .....
#     .....
#
#     z=-1
#     ..#..
#     .#..#
#     ....#
#     .#...
#     .....
#
#     z=0
#     ##...
#     ##...
#     #....
#     ....#
#     .###.
#
#     z=1
#     ..#..
#     .#..#
#     ....#
#     .#...
#     .....
#
#     z=2
#     .....
#     .....
#     ..#..
#     .....
#     .....
#
#
#     After 3 cycles:
#
#     z=-2
#     .......
#     .......
#     ..##...
#     ..###..
#     .......
#     .......
#     .......
#
#     z=-1
#     ..#....
#     ...#...
#     #......
#     .....##
#     .#...#.
#     ..#.#..
#     ...#...
#
#     z=0
#     ...#...
#     .......
#     #......
#     .......
#     .....##
#     .##.#..
#     ...#...
#
#     z=1
#     ..#....
#     ...#...
#     #......
#     .....##
#     .#...#.
#     ..#.#..
#     ...#...
#
#     z=2
#     .......
#     .......
#     ..##...
#     ..###..
#     .......
#     .......
#     .......
#
# After the full six-cycle boot process completes, 112 cubes are left in the
# active state.
#
# Starting with your given initial configuration, simulate six cycles. How 
# many cubes are left in the active state after the sixth cycle?
# -----------------------------------------------------------------------------------

import copy

slice_array = []
my_file = open('input.txt')
content = my_file.read()

slice_array = content.split("\n")
cycles = 6
#find dimension
largest = len(slice_array) + (2 * (cycles + 1))
z_large = 1 + (2 * (cycles + 1))

#create the array/lists for cube
cube_array = []
new_slice = []
new_row = []
z = 0
while z < z_large:
  x = 0
  new_slice.clear()
  while x < largest:
    y = 0
    new_row.clear()
    while y < largest:
      new_row.append(".")
      y = y + 1
    new_slice.append(copy.deepcopy(new_row))
    x = x + 1
  cube_array.append(copy.deepcopy(new_slice))
  z = z + 1

#insert the slice into cube cube_array
#cycles + 1 will be the center slice of z dimension
a = 0
while a < len(slice_array):
  b = 0
  strip = list(slice_array[a])
  while b < len(strip):
    cube_array[cycles + 1][cycles + 1 + a][cycles + 1 + b] = copy.deepcopy(strip[b])
    b = b + 1
  a = a + 1

#start the cycles
transfer_cube = copy.deepcopy(cube_array)
around = []
turn = 1
while turn <= cycles:
  #select cube
  c = 1
  while c < (len(cube_array) - 1):
    d = 1
    while d < (len(cube_array[c]) - 1):
      e = 1
      while e < (len(cube_array[c][d]) - 1):
        #append all the items around it
        f = -1
        around.clear()
        while f < 2:
          g = -1
          while g < 2:
            h = -1
            while h < 2:
              if (f != 0) or (g != 0) or (h !=0):
                around.append(cube_array[c+f][d+g][e+h])
              h = h + 1
            g = g + 1
          f = f + 1

        #count all the # items
        rad_count = 0
        j = 0
        while j < len(around):
          if around[j] == "#":
            rad_count = rad_count + 1
          j = j + 1
        
        #observe rules
        #put in new cube  array
        if cube_array[c][d][e] == "#":
          if rad_count == 2 or rad_count == 3:
            transfer_cube[c][d][e] = "#"
          else:
            transfer_cube[c][d][e] = "."
        else:
          if rad_count == 3:
            transfer_cube[c][d][e] = "#"
          else:
            transfer_cube[c][d][e] = "."
        e = e + 1
      d = d + 1
    c = c + 1
  #copy array to the old cube
  cube_array = copy.deepcopy(transfer_cube)

  turn = turn + 1

count = 0
c = 0
while c < len(cube_array):
  d = 0
  while d < len(cube_array[c]):
    e = 0
    while e < len(cube_array[c][d]):
      if cube_array[c][d][e] == "#":
        count = count + 1
      e = e + 1
    d = d + 1
  c = c + 1

print(count)
