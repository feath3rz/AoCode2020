# -----------------------------------------------------------------------------------
# --- Part Two ---
# The tile floor in the lobby is meant to be a living art exhibit. Every day,
# the tiles are all flipped according to the following rules:
#
#   - Any black tile with zero or more than 2 black tiles immediately 
#     adjacent to it is flipped to white.
#   - Any white tile with exactly 2 black tiles immediately adjacent to it 
#     is flipped to black.
#
# Here, tiles immediately adjacent means the six tiles directly touching the
# tile in question.
#
# The rules are applied simultaneously to every tile; put another way, it is 
# first determined which tiles need to be flipped, then they are all flipped 
# at the same time.
#
# In the above example, the number of black tiles that are facing up after 
# the given number of days has passed is as follows:
#
#     Day 1: 15
#     Day 2: 12
#     Day 3: 25
#     Day 4: 14
#     Day 5: 23
#     Day 6: 28
#     Day 7: 41
#     Day 8: 37
#     Day 9: 49
#     Day 10: 37
#     
#     Day 20: 132
#     Day 30: 259
#     Day 40: 406
#     Day 50: 566
#     Day 60: 788
#     Day 70: 1106
#     Day 80: 1373
#     Day 90: 1844
#     Day 100: 2208
#
# After executing this process a total of 100 times, there would be 2208 
# black tiles facing up.
#
# How many tiles will be black after 100 days?
# -----------------------------------------------------------------------------------

import copy

tile_array = []
my_file = open('input.txt')
content = my_file.read()

tile_array = content.split("\n")

#format the tiles array
i = 0
while i < len(tile_array):
  tile_array[i] = list(tile_array[i])
  i = i + 1

i = 0
while i < len(tile_array):
  j = 0
  while j < len(tile_array[i]):
    if tile_array[i][j] == 's' or tile_array[i][j] == 'n':
      tile_array[i][j] = ''.join(tile_array[i][j:j+2])
      tile_array[i].pop(j + 1)
    j = j + 1
  i = i + 1

tile_color = []

i = 0
while i < len(tile_array):
  x = 0
  y = 0
  j = 0
  #find the tile
  while j < len(tile_array[i]):
    if tile_array[i][j] == "e":
      x = x + 2
    elif tile_array[i][j] == "w":
      x = x - 2
    elif tile_array[i][j] == "ne":
      x = x + 1
      y = y + 1
    elif tile_array[i][j] == "nw":
      x = x - 1
      y = y + 1
    elif tile_array[i][j] == "se":
      x = x + 1
      y = y - 1
    elif tile_array[i][j] == "sw":
      x = x - 1
      y = y - 1
    j = j + 1
  
  #flip the tile
  if [x, y, "black"] in tile_color:
    tile_color.remove([x, y, "black"])
  else:
    tile_color.append([x, y, "black"])
    
  i = i + 1

#count the black tiles
print(len(tile_color))
#loop for 100 days
i = 0
new_set = []
while i < 100:
  #check every tile existing in the array
  j = 0
  new_set.clear()
  while j < len(tile_color):
    #Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
      #check surrounding tiles if they need flipping
    if [tile_color[j][0], tile_color[j][1], "black"] not in new_set and [tile_color[j][0], tile_color[j][1], "white"] not in new_set:
      black_tiles = 0
      if [tile_color[j][0] + 2, tile_color[j][1], "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] - 2, tile_color[j][1], "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] + 1, tile_color[j][1] + 1, "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] - 1, tile_color[j][1] + 1, "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] - 1, tile_color[j][1] - 1, "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] + 1, tile_color[j][1] - 1, "black"] in tile_color:
        black_tiles = black_tiles + 1
      
      if black_tiles == 0 or black_tiles > 2:
        new_set.append([copy.deepcopy(tile_color[j][0]), copy.deepcopy(tile_color[j][1]), "white"])
      else:
        new_set.append([copy.deepcopy(tile_color[j][0]), copy.deepcopy(tile_color[j][1]), "black"])

      #check east
    if [tile_color[j][0] + 2, tile_color[j][1], "black"] not in new_set and [tile_color[j][0] + 2, tile_color[j][1], "white"] not in new_set:
      black_tiles = 1
      if [tile_color[j][0] + 4, tile_color[j][1], "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] + 3, tile_color[j][1] + 1, "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] + 1, tile_color[j][1] + 1, "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] + 3, tile_color[j][1] - 1, "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] + 1, tile_color[j][1] - 1, "black"] in tile_color:
        black_tiles = black_tiles + 1
      
      if [tile_color[j][0] + 2, tile_color[j][1], "black"] in tile_color:
        if black_tiles > 2:
          new_set.append([copy.deepcopy(tile_color[j][0] + 2), copy.deepcopy(tile_color[j][1]), "white"])
        else:
          new_set.append([copy.deepcopy(tile_color[j][0] + 2), copy.deepcopy(tile_color[j][1]), "black"])
      elif black_tiles == 2:
        new_set.append([copy.deepcopy(tile_color[j][0] + 2), copy.deepcopy(tile_color[j][1]), "black"])
      

      #check west
    if [tile_color[j][0] - 2, tile_color[j][1], "black"] not in new_set and [tile_color[j][0] - 2, tile_color[j][1], "white"] not in new_set:
      black_tiles = 1
      if [tile_color[j][0] - 4, tile_color[j][1], "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] -1, tile_color[j][1] + 1, "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] -3, tile_color[j][1] + 1, "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] - 3, tile_color[j][1] - 1, "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] - 1, tile_color[j][1] - 1, "black"] in tile_color:
        black_tiles = black_tiles + 1

      if [tile_color[j][0] - 2, tile_color[j][1], "black"] in tile_color:
        if black_tiles > 2:
          new_set.append([copy.deepcopy(tile_color[j][0] - 2), copy.deepcopy(tile_color[j][1]), "white"])
        else:
          new_set.append([copy.deepcopy(tile_color[j][0] - 2), copy.deepcopy(tile_color[j][1]), "black"])
      elif black_tiles == 2:
        new_set.append([copy.deepcopy(tile_color[j][0] - 2), copy.deepcopy(tile_color[j][1]), "black"])


      #check ne
    if [tile_color[j][0] + 1, tile_color[j][1] + 1, "black"] not in new_set and [tile_color[j][0] + 1, tile_color[j][1] + 1, "white"] not in new_set:
      black_tiles = 1
      if [tile_color[j][0] + 3, tile_color[j][1] + 1, "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] - 1, tile_color[j][1] + 1, "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] + 2, tile_color[j][1] + 2, "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0], tile_color[j][1] + 2, "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] + 2, tile_color[j][1], "black"] in tile_color:
        black_tiles = black_tiles + 1
      
      if [tile_color[j][0] + 1, tile_color[j][1] + 1, "black"] in tile_color:
        if black_tiles > 2:
          new_set.append([copy.deepcopy(tile_color[j][0] + 1), copy.deepcopy(tile_color[j][1] + 1), "white"])
        else:
          new_set.append([copy.deepcopy(tile_color[j][0] + 1), copy.deepcopy(tile_color[j][1] + 1), "black"])
      elif black_tiles == 2:
        new_set.append([copy.deepcopy(tile_color[j][0] + 1), copy.deepcopy(tile_color[j][1] + 1), "black"])
      

      #check nw
    if [tile_color[j][0] - 1, tile_color[j][1] + 1, "black"] not in new_set and [tile_color[j][0] - 1, tile_color[j][1] + 1, "white"] not in new_set:
      black_tiles = 1
      if [tile_color[j][0] + 1, tile_color[j][1] + 1, "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] - 3, tile_color[j][1] + 1, "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0], tile_color[j][1] + 2, "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] - 2, tile_color[j][1] + 2, "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] - 2, tile_color[j][1], "black"] in tile_color:
        black_tiles = black_tiles + 1
      
      if [tile_color[j][0] - 1, tile_color[j][1] + 1, "black"] in tile_color:
        if black_tiles > 2:
          new_set.append([copy.deepcopy(tile_color[j][0] - 1), copy.deepcopy(tile_color[j][1] + 1), "white"])
        else:
          new_set.append([copy.deepcopy(tile_color[j][0] - 1), copy.deepcopy(tile_color[j][1] + 1), "black"])
      elif black_tiles == 2:
        new_set.append([copy.deepcopy(tile_color[j][0] - 1), copy.deepcopy(tile_color[j][1] + 1), "black"])

      
      #check se
    if [tile_color[j][0] + 1, tile_color[j][1] - 1, "black"] not in new_set and [tile_color[j][0] + 1, tile_color[j][1] - 1, "white"] not in new_set:
      black_tiles = 1
      if [tile_color[j][0] + 3, tile_color[j][1] - 1, "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] - 1, tile_color[j][1] - 1, "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] + 2, tile_color[j][1], "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] + 2, tile_color[j][1] - 2, "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0], tile_color[j][1] - 2, "black"] in tile_color:
        black_tiles = black_tiles + 1
      
      if [tile_color[j][0] + 1, tile_color[j][1] - 1, "black"] in tile_color:
        if black_tiles > 2:
          new_set.append([copy.deepcopy(tile_color[j][0] + 1), copy.deepcopy(tile_color[j][1] - 1), "white"])
        else:
          new_set.append([copy.deepcopy(tile_color[j][0] + 1), copy.deepcopy(tile_color[j][1] - 1), "black"])
      elif black_tiles == 2:
        new_set.append([copy.deepcopy(tile_color[j][0] + 1), copy.deepcopy(tile_color[j][1] - 1), "black"])
      
      
      #check sw
    if [tile_color[j][0] - 1, tile_color[j][1] - 1, "black"] not in new_set and [tile_color[j][0] - 1, tile_color[j][1] - 1, "white"] not in new_set:
      black_tiles = 1
      if [tile_color[j][0] + 1, tile_color[j][1] - 1, "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] - 3, tile_color[j][1] - 1, "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] - 2, tile_color[j][1], "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0], tile_color[j][1] - 2, "black"] in tile_color:
        black_tiles = black_tiles + 1
      if [tile_color[j][0] - 2, tile_color[j][1] - 2, "black"] in tile_color:
        black_tiles = black_tiles + 1
      
      if [tile_color[j][0] - 1, tile_color[j][1] - 1, "black"] in tile_color:
        if black_tiles > 2:
          new_set.append([copy.deepcopy(tile_color[j][0] - 1), copy.deepcopy(tile_color[j][1] - 1), "white"])
        else:
          new_set.append([copy.deepcopy(tile_color[j][0] - 1), copy.deepcopy(tile_color[j][1] - 1), "black"])
      elif black_tiles == 2:
        new_set.append([copy.deepcopy(tile_color[j][0] - 1), copy.deepcopy(tile_color[j][1] - 1), "black"])

    if j % 100 == 0:
      print(i, "-", j)
    j = j + 1
  
  l = 0
  while l < len(new_set):
    if new_set[l][2] == "white":
      new_set.pop(l)
    else:
      l = l + 1
  
  tile_color.clear()
  tile_color = copy.deepcopy(new_set)
  i = i + 1

print(len(tile_color))
