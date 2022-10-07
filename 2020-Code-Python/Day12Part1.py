# -----------------------------------------------------------------------------------
# https://adventofcode.com/2020/day/12
# 
# --- Day 12: Rain Risk ---
# Your ferry made decent progress toward the island, but the storm came in 
# faster than anyone expected. The ferry needs to take evasive actions!
#
# Unfortunately, the ship's navigation computer seems to be malfunctioning; 
# rather than giving a route directly to safety, it produced extremely 
# circuitous instructions. When the captain uses the PA system to ask if 
# anyone can help, you quickly volunteer.
#
# The navigation instructions (your puzzle input) consists of a sequence of 
# single-character actions paired with integer input values. After staring at 
# them for a few minutes, you work out what they probably mean:
#
#   - Action N means to move north by the given value.
#   - Action S means to move south by the given value.
#   - Action E means to move east by the given value.
#   - Action W means to move west by the given value.
#   - Action L means to turn left the given number of degrees.
#   - Action R means to turn right the given number of degrees.
#   - Action F means to move forward by the given value in the direction the
#     ship is currently facing.
#
# The ship starts by facing east. Only the L and R actions change the 
# direction the ship is facing. (That is, if the ship is facing east and the
# next instruction is N10, the ship would move north 10 units, but would 
# still move east if the following action were F.)
#
# For example:
#
#     F10
#     N3
#     F7
#     R90
#     F11
#
# These instructions would be handled as follows:
#
#   - F10 would move the ship 10 units east (because the ship starts by 
#     facing east) to east 10, north 0.
#   - N3 would move the ship 3 units north to east 10, north 3.
#   - F7 would move the ship another 7 units east (because the ship is still 
#     facing east) to east 17, north 3.
#   - R90 would cause the ship to turn right by 90 degrees and face south;
#     it remains at east 17, north 3.
#   - F11 would move the ship 11 units south to east 17, south 8.
#
# At the end of these instructions, the ship's Manhattan distance (sum of the
# absolute values of its east/west position and its north/south position) 
# from its starting position is 17 + 8 = 25.
#
# Figure out where the navigation instructions lead. What is the Manhattan 
# distance between that location and the ship's starting position?
# -----------------------------------------------------------------------------------

nav_array = []
my_file = open('input.txt')
content = my_file.read()

nav_array = content.split("\n")

boat_face = 0
y_dir = 0
x_dir = 0
i = 0

while i < len(nav_array):
  curr_nav = list(nav_array[i])
  curr_inst = curr_nav[0]
  curr_num = int("".join(curr_nav[1:len(curr_nav)]))

  if curr_inst == "F":
    if boat_face == 0:
      x_dir = x_dir + curr_num
    elif boat_face == 90:
      y_dir = y_dir + curr_num
    elif boat_face == 180:
      x_dir = x_dir - curr_num
    elif boat_face == 270:
      y_dir = y_dir - curr_num
    else:
      print("Error: boat_face incorrect number")
    
  elif curr_inst == "N":
    y_dir = y_dir + curr_num
  elif curr_inst == "S":
    y_dir = y_dir - curr_num
  elif curr_inst == "E":
    x_dir = x_dir + curr_num
  elif curr_inst == "W":
    x_dir = x_dir - curr_num

  elif curr_inst == "L":
    boat_face = boat_face + curr_num
    while boat_face >= 360:
      boat_face = boat_face - 360

  elif curr_inst == "R":
    boat_face = boat_face - curr_num
    while boat_face < 0:
      boat_face = boat_face + 360

  i = i + 1

print(abs(x_dir) + abs(y_dir))
