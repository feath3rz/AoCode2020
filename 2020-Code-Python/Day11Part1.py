# -----------------------------------------------------------------------------------
# https://adventofcode.com/2020/day/11
#
# --- Day 11: Seating System ---
# Your plane lands with plenty of time to spare. The final leg of your 
# journey is a ferry that goes directly to the tropical island where you can 
# finally start your vacation. As you reach the waiting area to board the 
# ferry, you realize you're so early, nobody else has even arrived yet!
#
# By modeling the process people use to choose (or abandon) their seat in the 
# waiting area, you're pretty sure you can predict the best place to sit. You 
# make a quick map of the seat layout (your puzzle input).
#
# The seat layout fits neatly on a grid. Each position is either floor (.), 
# an empty seat (L), or an occupied seat (#). For example, the initial seat 
# layout might look like this:
#
#     L.LL.LL.LL
#     LLLLLLL.LL
#     L.L.L..L..
#     LLLL.LL.LL
#     L.LL.LL.LL
#     L.LLLLL.LL
#     ..L.L.....
#     LLLLLLLLLL
#     L.LLLLLL.L
#     L.LLLLL.LL
#
# Now, you just need to model the people who will be arriving shortly. 
# Fortunately, people are entirely predictable and always follow a simple set
# of rules. All decisions are based on the number of occupied seats adjacent 
# to a given seat (one of the eight positions immediately up, down, left, 
# right, or diagonal from the seat). The following rules are applied to every
# seat simultaneously:
#
#   - If a seat is empty (L) and there are no occupied seats adjacent to it, 
#     the seat becomes occupied.
#   - If a seat is occupied (#) and four or more seats adjacent to it are 
#     also occupied, the seat becomes empty.
#   - Otherwise, the seat's state does not change.
#
# Floor (.) never changes; seats don't move, and nobody sits on the floor.
#
# After one round of these rules, every seat in the example layout becomes 
# occupied:
#
#     #.##.##.##
#     #######.##
#     #.#.#..#..
#     ####.##.##
#     #.##.##.##
#     #.#####.##
#     ..#.#.....
#     ##########
#     #.######.#
#     #.#####.##
#
# After a second round, the seats with four or more occupied adjacent seats 
# become empty again:
#
#     #.LL.L#.##
#     #LLLLLL.L#
#     L.L.L..L..
#     #LLL.LL.L#
#     #.LL.LL.LL
#     #.LLLL#.##
#     ..L.L.....
#     #LLLLLLLL#
#     #.LLLLLL.L
#     #.#LLLL.##
#
# This process continues for three more rounds:
#
#     #.##.L#.##
#     #L###LL.L#
#     L.#.#..#..
#     #L##.##.L#
#     #.##.LL.LL
#     #.###L#.##
#     ..#.#.....
#     #L######L#
#     #.LL###L.L
#     #.#L###.##
#
#     #.#L.L#.##
#     #LLL#LL.L#
#     L.L.L..#..
#     #LLL.##.L#
#     #.LL.LL.LL
#     #.LL#L#.##
#     ..L.L.....
#     #L#LLLL#L#
#     #.LLLLLL.L
#     #.#L#L#.##
#
#     #.#L.L#.##
#     #LLL#LL.L#
#     L.#.L..#..
#     #L##.##.L#
#     #.#L.LL.LL
#     #.#L#L#.##
#     ..L.L.....
#     #L#L##L#L#
#     #.LLLLLL.L
#     #.#L#L#.##
#
# At this point, something interesting happens: the chaos stabilizes and 
# further applications of these rules cause no seats to change state! Once 
# people stop moving around, you count 37 occupied seats.
#
# Simulate your seating area by applying the seating rules repeatedly until 
# no seats change state. How many seats end up occupied?
# -----------------------------------------------------------------------------------

row_array = []
my_file = open('input.txt')
content = my_file.read()

row_array = content.split("\n")
t = 0
mass_row = []

while t < len(row_array):
  mass_row.append(list(row_array[t]))
  t = t + 1


def add_seats(the_symbol, the_test, no_change, the_change, the_incre):
  x_start = curr_row - 1
  x_end = curr_row + 1
  y_end = rows + 1
  all_symbols = []
  all_symbols.clear()
  do_again = False
  while (x_start <= x_end):
    y_start = rows - 1
    while (x_start >= 0) and (x_start < len(mass_row[rows])) and (y_start <= y_end) and (y_start < len(row_array)):
      if ((y_start != rows) or (x_start != curr_row)) and (y_start >= 0):
        all_symbols.append(mass_row[y_start][x_start])
      y_start = y_start + 1
    x_start = x_start + 1
  sym_check = 0
  sym_count = 0
  while sym_check < len(all_symbols):
    if all_symbols[sym_check] == the_test:
      sym_count = sym_count + 1
    sym_check = sym_check + 1

  if sym_count >= the_incre:
    if the_symbol == "#":
      do_again = True
    return no_change, do_again
  else:
    if the_symbol == "L":
      do_again = True
    return the_change, do_again


again = True
changed = False

while again == True:
  again = False
  rows1, cols1 = (len(row_array), len(mass_row[0]))
  new_mass = [["." for i in range(cols1)] for j in range(rows1)]
  rows = 0
  while rows < len(mass_row):
    curr_row = 0
    while curr_row < len(mass_row[rows]):
      if mass_row[rows][curr_row] == "#":
        symbol, changed = add_seats("#", "#", "L", "#", 4)
        new_mass[rows][curr_row] = symbol
      elif mass_row[rows][curr_row] == "L":
        symbol, changed = add_seats("L", "#", "L", "#", 1)
        new_mass[rows][curr_row] = symbol

      if changed == True:
        again = True
      curr_row = curr_row + 1
    rows = rows + 1
  mass_row = new_mass




r = 0
s = 0
count = 0

while r < len(mass_row):
  s = 0
  while s < len(mass_row[r]):
    if mass_row[r][s] == "#":
      count = count + 1
    s = s + 1
  r = r + 1
print(count)
print("done")
