# -----------------------------------------------------------------------------------
# --- Part Two ---
# The Elves in accounting are thankful for your help; one of them even offers 
# you a starfish coin they had left over from a past vacation. They offer you 
# a second one if you can find three numbers in your expense report that meet 
# the same criteria.
#
# Using the above example again, the three entries that sum to 2020 are 979, 
# 366, and 675. Multiplying them together produces the answer, 241861950.
#
# In your expense report, what is the product of the three entries that sum to 2020?
# -----------------------------------------------------------------------------------

entry_array = []
with open('data.txt') as amounts:
    for line in amounts:
        entry_array.append(int(line))

my_position = 0
second_position = 0
third_position = 0
check_one = 0
check_two = 0
num1 = 0
num2 = 0
num3 = 0

while my_position < len(entry_array):
  check_one = 2020 - entry_array[my_position]
  second_position = my_position + 1

  while second_position < len(entry_array):
    check_two = check_one - entry_array[second_position]
    third_position = second_position + 1

    while third_position < len(entry_array):
      if check_two == entry_array[third_position]:
        num1 = entry_array[my_position]
        num2 = entry_array[second_position]
        num3 = check_two
        third_position = len(entry_array)
        second_position = len(entry_array)
        my_position = len(entry_array)
      else:
        third_position = third_position + 1

    second_position = second_position + 1

  my_position = my_position + 1

print (num1 * num2 * num3)
