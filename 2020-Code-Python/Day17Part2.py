# -----------------------------------------------------------------------------------
# --- Part Two ---
# For some reason, your simulated results don't match what the experimental 
# energy source engineers expected. Apparently, the pocket dimension actually
# has four spatial dimensions, not three.
#
# The pocket dimension contains an infinite 4-dimensional grid. At every 
# integer 4-dimensional coordinate (x,y,z,w), there exists a single cube 
# (really, a hypercube) which is still either active or inactive.
#
# Each cube only ever considers its neighbors: any of the 80 other cubes 
# where any of their coordinates differ by at most 1. For example, given the 
# cube at x=1,y=2,z=3,w=4, its neighbors include the cube at x=2,y=2,z=3,w=3, 
# the cube at x=0,y=2,z=3,w=4, and so on.
#
# The initial state of the pocket dimension still consists of a small flat 
# region of cubes. Furthermore, the same rules for cycle updating still 
# apply: during each cycle, consider the number of active neighbors of each cube.
#
# For example, consider the same initial state as in the example above. Even 
# though the pocket dimension is 4-dimensional, this initial state represents
# a small 2-dimensional slice of it. (In particular, this initial state 
# defines a 3x3x1x1 region of the 4-dimensional space.)
#
# Simulating a few cycles from this initial state produces the following 
# configurations, where the result of each cycle is shown layer-by-layer at 
# each given z and w coordinate:
#
#     Before any cycles:
#
#     z=0, w=0
#     .#.
#     ..#
#     ###
#
#
#     After 1 cycle:
#
#     z=-1, w=-1
#     #..
#     ..#
#     .#.
#
#     z=0, w=-1
#     #..
#     ..#
#     .#.
#
#     z=1, w=-1
#     #..
#     ..#
#     .#.
#
#     z=-1, w=0
#     #..
#     ..#
#     .#.
#
#     z=0, w=0
#     #.#
#     .##
#     .#.
#
#     z=1, w=0
#     #..
#     ..#
#     .#.
#
#     z=-1, w=1
#     #..
#     ..#
#     .#.
#
#     z=0, w=1
#     #..
#     ..#
#     .#.
#
#     z=1, w=1
#     #..
#     ..#
#     .#.
#
#
#     After 2 cycles:
#
#     z=-2, w=-2
#     .....
#     .....
#     ..#..
#     .....
#     .....
#
#     z=-1, w=-2
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=0, w=-2
#     ###..
#     ##.##
#     #...#
#     .#..#
#     .###.
#
#     z=1, w=-2
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=2, w=-2
#     .....
#     .....
#     ..#..
#     .....
#     .....
#
#     z=-2, w=-1
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=-1, w=-1
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=0, w=-1
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=1, w=-1
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=2, w=-1
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=-2, w=0
#     ###..
#     ##.##
#     #...#
#     .#..#
#     .###.
#
#     z=-1, w=0
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=0, w=0
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=1, w=0
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=2, w=0
#     ###..
#     ##.##
#     #...#
#     .#..#
#     .###.
#
#     z=-2, w=1
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=-1, w=1
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=0, w=1
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=1, w=1
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=2, w=1
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=-2, w=2
#     .....
#     .....
#     ..#..
#     .....
#     .....
#
#     z=-1, w=2
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=0, w=2
#     ###..
#     ##.##
#     #...#
#     .#..#
#     .###.
#
#     z=1, w=2
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=2, w=2
#     .....
#     .....
#     ..#..
#     .....
#     .....
#
# After the full six-cycle boot process completes, 848 cubes are left in the
# active state.
#
# Starting with your given initial configuration, simulate six cycles in a 4-
# dimensional space. How many cubes are left in the active state after the
# sixth cycle?
# -----------------------------------------------------------------------------------
# This code takes a long time, but it works
# -----------------------------------------------------------------------------------


import copy

slice_array = []
my_file = open('input.txt')
content = my_file.read()

slice_array = content.split("\n")
cycles = 6
#find dimension
#label the input items:
a = 0
start_array = []
while a < len(slice_array):
  start_array.append(list(slice_array[a]))
  a = a + 1

def check_cube(m, n, o, p, curr_array):
  count_active = 0
  q = p - 1
  while q <= p + 1:
    r = o - 1
    while r <= o + 1:
      s = n - 1
      while s <= n + 1:
        t = m - 1
        while t <= m + 1:
          if [t, s, r, q, "active"] in curr_array:
            count_active = count_active + 1
          t = t + 1
        s = s + 1
      r = r + 1
    q = q + 1
  if [m, n, o, p, "active"] in curr_array:
    count_active = count_active - 1
    if count_active == 2 or count_active == 3:
      return [m, n, o, p, "active"]
    else:
      return [m, n, o, p, "inactive"]
  else:
    if count_active == 3:
      return [m, n, o, p, "active"]
    else:
      return[m, n, o, p, "inactive"]

active_array = []
a = 0
c = 0
d = 0
while a < len(start_array):
  b = 0
  while b < len(start_array[a]):
    if start_array[a][b] == "#":
      active_array.append([a, b, c, d, "active"])
    b = b + 1
  a = a + 1


temp_array = []

while cycles > 0:
  i = 0
  temp_array.clear()
  while i < len(active_array):
    #check all the cubes around the active cubes
    d = active_array[i][3] - 1
    while d <= active_array[i][3] + 1:
      c = active_array[i][2] - 1
      while c <= active_array[i][2] + 1:
        b = active_array[i][1] - 1
        while b <= active_array[i][1] + 1:
          a = active_array[i][0] - 1
          while a <= active_array[i][0] + 1:
            if a == active_array[i][0] and b == active_array[i][1] and c == active_array[i][2] and d == active_array[i][3]:
              a = a + 1
            else:
              if [a, b, c, d, "active"] not in temp_array and [a, b, c, d, "inactive"] not in temp_array:
                temp_array.append(check_cube(a, b, c, d, active_array))
              a = a + 1
          b = b + 1
        c = c + 1
      d = d + 1
    i = i + 1
  
  active_array.clear()
  k = 0
  while k < len(temp_array):
    if temp_array[k] not in active_array:
      active_array.append(copy.deepcopy(temp_array[k]))
    k = k + 1
  
  l = 0
  while l < len(active_array):
    if active_array[l][4] == "inactive":
      active_array.pop(l)
    else:
      l = l + 1

  cycles = cycles - 1

print(len(active_array))
