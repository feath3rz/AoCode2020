# -----------------------------------------------------------------------------------
# --- Part Two ---
# Before you can give the destination to the captain, you realize that the 
# actual action meanings were printed on the back of the instructions the 
# whole time.
#
# Almost all of the actions indicate how to move a waypoint which is relative
# to the ship's position:
#
#   - Action N means to move the waypoint north by the given value.
#   - Action S means to move the waypoint south by the given value.
#   - Action E means to move the waypoint east by the given value.
#   - Action W means to move the waypoint west by the given value.
#   - Action L means to rotate the waypoint around the ship left (counter-
#     clockwise) the given number of degrees.
#   - Action R means to rotate the waypoint around the ship right 
#     (clockwise) the given number of degrees.
#   - Action F means to move forward to the waypoint a number of times equal
#     to the given value.
#
# The waypoint starts 10 units east and 1 unit north relative to the ship.
# The waypoint is relative to the ship; that is, if the ship moves, the 
# waypoint moves with it.
#
# For example, using the same instructions as above:
#
#   - F10 moves the ship to the waypoint 10 times (a total of 100 units east
#     and 10 units north), leaving the ship at east 100, north 10. The 
#     waypoint stays 10 units east and 1 unit north of the ship.
#   - N3 moves the waypoint 3 units north to 10 units east and 4 units north 
#     of the ship. The ship remains at east 100, north 10.
#   - F7 moves the ship to the waypoint 7 times (a total of 70 units east 
#     and 28 units north), leaving the ship at east 170, north 38. The 
#     waypoint stays 10 units east and 4 units north of the ship.
#   - R90 rotates the waypoint around the ship clockwise 90 degrees, moving
#     it to 4 units east and 10 units south of the ship. The ship remains at 
#     east 170, north 38.
#   - F11 moves the ship to the waypoint 11 times (a total of 44 units east
#     and 110 units south), leaving the ship at east 214, south 72. The 
#     waypoint stays 4 units east and 10 units south of the ship.
#
# After these operations, the ship's Manhattan distance from its starting 
# position is 214 + 72 = 286.
#
# Figure out where the navigation instructions actually lead. What is the 
# Manhattan distance between that location and the ship's starting position?
# -----------------------------------------------------------------------------------

nav_array = []
my_file = open('input.txt')
content = my_file.read()

nav_array = content.split("\n")

y_dir = 0
x_dir = 0
waypoint_x = 10
waypoint_y = 1
temp_x = 0

i = 0

while i < len(nav_array):
  curr_nav = list(nav_array[i])
  curr_inst = curr_nav[0]
  curr_num = int("".join(curr_nav[1:len(curr_nav)]))

  print("boat is: ", x_dir, ", ", y_dir)
  print("waypoint is: ", waypoint_x, ", ", waypoint_y)
  print("instructions: ", curr_inst, ", ", curr_num)

  if curr_inst == "F":
    x_move = (waypoint_x - x_dir) * curr_num
    y_move = (waypoint_y - y_dir) * curr_num
    x_dir = x_dir + x_move
    y_dir = y_dir + y_move
    waypoint_x = waypoint_x + x_move
    waypoint_y = waypoint_y + y_move
    
  elif curr_inst == "N":
    waypoint_y = waypoint_y + curr_num
  elif curr_inst == "S":
    waypoint_y = waypoint_y - curr_num
  elif curr_inst == "E":
    waypoint_x = waypoint_x + curr_num
  elif curr_inst == "W":
    waypoint_x = waypoint_x - curr_num

  elif curr_inst == "L":
    temp_x = waypoint_x
    if curr_num == 90:
      waypoint_x = x_dir - (waypoint_y - y_dir)
      waypoint_y = y_dir + (temp_x - x_dir)
    elif curr_num == 180:
      waypoint_x = x_dir - (waypoint_x - x_dir)
      waypoint_y = y_dir - (waypoint_y - y_dir)
    elif curr_num == 270:
      waypoint_x = x_dir + (waypoint_y - y_dir)
      waypoint_y = y_dir - (temp_x - x_dir)

  elif curr_inst == "R":
    temp_x = waypoint_x
    if curr_num == 270:
      waypoint_x = x_dir - (waypoint_y - y_dir)
      waypoint_y = y_dir + (temp_x - x_dir)
    elif curr_num == 180:
      waypoint_x = x_dir - (waypoint_x - x_dir)
      waypoint_y = y_dir - (waypoint_y - y_dir)
    elif curr_num == 90:
      waypoint_x = x_dir + (waypoint_y - y_dir)
      waypoint_y = y_dir - (temp_x - x_dir)

  print("boat is: ", x_dir, ", ", y_dir)
  print("waypoint is: ", waypoint_x, ", ", waypoint_y)

  i = i + 1

print(abs(x_dir) + abs(y_dir))
