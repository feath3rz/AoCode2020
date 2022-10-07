# -----------------------------------------------------------------------------------
# https://adventofcode.com/2020/day/24
#
# --- Day 24: Lobby Layout ---
# Your raft makes it to the tropical island; it turns out that the small crab 
# was an excellent navigator. You make your way to the resort.
#
# As you enter the lobby, you discover a small problem: the floor is being 
# renovated. You can't even reach the check-in desk until they've finished
# installing the new tile floor.
#
# The tiles are all hexagonal; they need to be arranged in a hex grid with a 
# very specific color pattern. Not in the mood to wait, you offer to help 
# figure out the pattern.
#
# The tiles are all white on one side and black on the other. They start with
# the white side facing up. The lobby is large enough to fit whatever pattern 
# might need to appear there.
#
# A member of the renovation crew gives you a list of the tiles that need to
# be flipped over (your puzzle input). Each line in the list identifies a
# single tile that needs to be flipped by giving a series of steps starting
# from a reference tile in the very center of the room. (Every line starts
# from the same reference tile.)
#
# Because the tiles are hexagonal, every tile has six neighbors: east, 
# southeast, southwest, west, northwest, and northeast. These directions are
# given in your list, respectively, as e, se, sw, w, nw, and ne. A tile is 
# identified by a series of these directions with no delimiters; for example, 
# esenee identifies the tile you land on if you start at the reference tile
# and then move one tile east, one tile southeast, one tile northeast, and 
# one tile east.
#
# Each time a tile is identified, it flips from white to black or from black
# to white. Tiles might be flipped more than once. For example, a line like 
# esew flips a tile immediately adjacent to the reference tile, and a line 
# like nwwswee flips the reference tile itself.
#
# Here is a larger example:
#
#     sesenwnenenewseeswwswswwnenewsewsw
#     neeenesenwnwwswnenewnwwsewnenwseswesw
#     seswneswswsenwwnwse
#     nwnwneseeswswnenewneswwnewseswneseene
#     swweswneswnenwsewnwneneseenw
#     eesenwseswswnenwswnwnwsewwnwsene
#     sewnenenenesenwsewnenwwwse
#     wenwwweseeeweswwwnwwe
#     wsweesenenewnwwnwsenewsenwwsesesenwne
#     neeswseenwwswnwswswnw
#     nenwswwsewswnenenewsenwsenwnesesenew
#     enewnwewneswsewnwswenweswnenwsenwsw
#     sweneswneswneneenwnewenewwneswswnese
#     swwesenesewenwneswnwwneseswwne
#     enesenwswwswneneswsenwnewswseenwsese
#     wnwnesenesenenwwnenwsewesewsesesew
#     nenewswnwewswnenesenwnesewesw
#     eneswnwswnwsenenwnwnwwseeswneewsenese
#     neswnwewnwnwseenwseesewsenwsweewe
#     wseweeenwnesenwwwswnew
# 
# In the above example, 10 tiles are flipped once (to black), and 5 more are 
# flipped twice (to black, then back to white). After all of these 
# instructions have been followed, a total of 10 tiles are black.
#
# Go through the renovation crew's list and determine which tiles they need 
# to flip. After all of the instructions have been followed, how many tiles
# are left with the black side up?
# -----------------------------------------------------------------------------------

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
