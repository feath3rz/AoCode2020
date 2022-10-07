# -----------------------------------------------------------------------------------
# --- Part Two ---
# Ding! The "fasten seat belt" signs have turned on. Time to find your seat.
#
# It's a completely full flight, so your seat should be the only missing 
# boarding pass in your list. However, there's a catch: some of the seats at 
# the very front and back of the plane don't exist on this aircraft, so 
# they'll be missing from your list as well.
#
# Your seat wasn't at the very front or back, though; the seats with IDs +1
# and -1 from yours will be in your list.
#
# What is the ID of your seat?
# -----------------------------------------------------------------------------------


seat_array = []
allIDs = []
my_file = open('input.txt')
content = my_file.read()

seat_array = content.split("\n")
i = 0
min_seat = 0
max_seat = 127
seat_poss = 0
myID = 0

rows, cols = (128, 8) 
all_seats = [[False for i in range(cols)] for j in range(rows)]

while i < len(seat_array):
  find_seat = list(seat_array[i])
  min_seat = 0
  max_seat = 127
  while seat_poss <= 6:
    if find_seat[seat_poss] == "F":
      max_seat = (min_seat + max_seat) // 2
    elif find_seat[seat_poss] == "B":
      min_seat = ((min_seat + max_seat) // 2) + 1
    seat_poss = seat_poss + 1
  
  vert_seat = (min_seat + max_seat) // 2
  
  if (vert_seat != 0) and (vert_seat != 127):
    min_seat = 0
    max_seat = 7
    while seat_poss <= 9:
      if find_seat[seat_poss] == "L":
       max_seat = (min_seat + max_seat) // 2
      elif find_seat[seat_poss] == "R":
       min_seat = ((min_seat + max_seat) // 2) + 1
      seat_poss = seat_poss + 1
  
    horr_seat = (min_seat + max_seat) // 2
    currID = (vert_seat * 8) + horr_seat
    allIDs.append(currID)
    all_seats[vert_seat][horr_seat] = True

  i = i + 1
  seat_poss = 0


vert_seat = 1
horr_seat = 0
while vert_seat < 127:
  while horr_seat < 8:
    if all_seats[vert_seat][horr_seat] == False:
      currID = (vert_seat * 8) + horr_seat
      if (currID + 1 in allIDs) and (currID - 1 in allIDs):
        mySeat = currID
        vert_seat = 127
        horr_seat = 8
    horr_seat = horr_seat + 1
  horr_seat = 0
  vert_seat = vert_seat + 1
      
print(mySeat)
