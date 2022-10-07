# -----------------------------------------------------------------------------------
# --- Part Two ---
# As soon as people start to arrive, you realize your mistake. People don't 
# just care about adjacent seats - they care about the first seat they can 
# see in each of those eight directions!
#
# Now, instead of considering just the eight immediately adjacent seats,
# consider the first seat in each of those eight directions. For example, the
# empty seat below would see eight occupied seats:
#
#     .......#.
#     ...#.....
#     .#.......
#     .........
#     ..#L....#
#     ....#....
#     .........
#     #........
#     ...#.....
#
# The leftmost empty seat below would only see one empty seat, but cannot see
# any of the occupied ones:
#
#     .............
#     .L.L.#.#.#.#.
#     .............
#
# The empty seat below would see no occupied seats:
#
#     .##.##.
#     #.#.#.#
#     ##...##
#     ...L...
#     ##...##
#     #.#.#.#
#     .##.##.
#
# Also, people seem to be more tolerant than you expected: it now takes five 
# or more visible occupied seats for an occupied seat to become empty (rather 
# than four or more from the previous rules). The other rules still apply:
# empty seats that see no occupied seats become occupied, seats matching no 
# rule don't change, and floor never changes.
#
# Given the same starting layout as above, these new rules cause the seating 
# area to shift around as follows:
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
#     #.LL.LL.L#
#     #LLLLLL.LL
#     L.L.L..L..
#     LLLL.LL.LL
#     L.LL.LL.LL
#     L.LLLLL.LL
#     ..L.L.....
#     LLLLLLLLL#
#     #.LLLLLL.L
#     #.LLLLL.L#
#
#     #.L#.##.L#
#     #L#####.LL
#     L.#.#..#..
#     ##L#.##.##
#     #.##.#L.##
#     #.#####.#L
#     ..#.#.....
#     LLL####LL#
#     #.L#####.L
#     #.L####.L#
#
#     #.L#.L#.L#
#     #LLLLLL.LL
#     L.L.L..#..
#     ##LL.LL.L#
#     L.LL.LL.L#
#     #.LLLLL.LL
#     ..L.L.....
#     LLLLLLLLL#
#     #.LLLLL#.L
#     #.L#LL#.L#
#
#     #.L#.L#.L#
#     #LLLLLL.LL
#     L.L.L..#..
#     ##L#.#L.L#
#     L.L#.#L.L#
#     #.L####.LL
#     ..#.#.....
#     LLL###LLL#
#     #.LLLLL#.L
#     #.L#LL#.L#
#
#     #.L#.L#.L#
#     #LLLLLL.LL
#     L.L.L..#..
#     ##L#.#L.L#
#     L.L#.LL.L#
#     #.LLLL#.LL
#     ..#.L.....
#     LLL###LLL#
#     #.LLLLL#.L
#     #.L#LL#.L#
#
# Again, at this point, people stop shifting around and the seating area 
# reaches equilibrium. Once this occurs, you count 26 occupied seats.
#
# Given the new visibility method and the rule change for occupied seats 
# becoming empty, once equilibrium is reached, how many seats end up 
# occupied?
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

change = True
rows1, cols1 = (len(row_array), len(mass_row[0]))
new_mass = [["." for i in range(cols1)] for j in range(rows1)]


while change == True:
  i = 0
  change = False
  while i < len(mass_row):
    j = 0
    while j < len(mass_row[i]):
      all_symbols = []
      all_symbols.clear()

      if mass_row[i][j] == ".":
        new_mass[i][j] = "."
      else:
        #north
        x_poss = j
        y_poss = i - 1
        found_sym = False
        while (found_sym == False) and (y_poss >= 0):
          curr_check = mass_row[y_poss][x_poss]
          if curr_check != ".":
            all_symbols.append(curr_check)
            found_sym = True
          y_poss = y_poss - 1

        #north-east
        found_sym = False
        x_poss = j + 1
        y_poss = i - 1
        while (found_sym == False) and (y_poss >= 0) and (x_poss < len(mass_row[i])):
          curr_check = mass_row[y_poss][x_poss]
          if curr_check != ".":
            all_symbols.append(curr_check)
            found_sym = True
          y_poss = y_poss - 1
          x_poss = x_poss + 1

        #north-west
        found_sym = False
        x_poss = j - 1
        y_poss = i - 1
        while (found_sym == False) and (y_poss >= 0) and (x_poss >= 0):
          curr_check = mass_row[y_poss][x_poss]
          if curr_check != ".":
            all_symbols.append(curr_check)
            found_sym = True
          y_poss = y_poss - 1
          x_poss = x_poss - 1

        #west
        found_sym = False
        x_poss = j - 1
        y_poss = i
        while (found_sym == False) and (x_poss >= 0):
          curr_check = mass_row[y_poss][x_poss]
          if curr_check != ".":
            all_symbols.append(curr_check)
            found_sym = True
          x_poss = x_poss - 1

        #east
        found_sym = False
        x_poss = j + 1
        y_poss = i
        while (found_sym == False) and (x_poss < len(mass_row[i])):
          curr_check = mass_row[y_poss][x_poss]
          if curr_check != ".":
            all_symbols.append(curr_check)
            found_sym = True
          x_poss = x_poss + 1

        #south
        x_poss = j
        y_poss = i + 1
        found_sym = False
        while (found_sym == False) and (y_poss < len(mass_row)):
          curr_check = mass_row[y_poss][x_poss]
          if curr_check != ".":
            all_symbols.append(curr_check)
            found_sym = True
          y_poss = y_poss + 1

        #south-east
        found_sym = False
        x_poss = j + 1
        y_poss = i + 1
        while (found_sym == False) and (y_poss < len(mass_row)) and (x_poss < len(mass_row[i])):
          curr_check = mass_row[y_poss][x_poss]
          if curr_check != ".":
            all_symbols.append(curr_check)
            found_sym = True
          y_poss = y_poss + 1
          x_poss = x_poss + 1

        #south-west
        found_sym = False
        x_poss = j - 1
        y_poss = i + 1
        while (found_sym == False) and (y_poss < len(mass_row)) and (x_poss >= 0):
          curr_check = mass_row[y_poss][x_poss]
          if curr_check != ".":
            all_symbols.append(curr_check)
            found_sym = True
          y_poss = y_poss + 1
          x_poss = x_poss - 1

        #count occupied
        occu_count = 0
        k = 0
        while k < len(all_symbols):
          if all_symbols[k] == "#":
            occu_count = occu_count + 1
          k = k + 1
        #find if it has stuff and if change
        if mass_row[i][j] == "L":
          if occu_count == 0:
            new_mass[i][j] = "#"
            change = True
          else:
            new_mass[i][j] = "L"
        elif mass_row[i][j] == "#":
          if occu_count >= 5:
            new_mass[i][j] = "L"
            change = True
          else:
            new_mass[i][j] = "#"
      j = j + 1
    i = i + 1

  l = 0
  while l < len(mass_row):
    m = 0
    while m < len(mass_row[l]):
      mass_row[l][m] = new_mass[l][m]
      m = m + 1
    l = l + 1

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
