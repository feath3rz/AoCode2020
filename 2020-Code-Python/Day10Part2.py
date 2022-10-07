# -----------------------------------------------------------------------------------
# --- Part Two ---
# To completely determine whether you have enough adapters, you'll need to
# figure out how many different ways they can be arranged. Every arrangement 
# needs to connect the charging outlet to your device. The previous rules
# about when adapters can successfully connect still apply.
#
# The first example above (the one that starts with 16, 10, 15) supports the 
# following arrangements:
#
#     (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
#     (0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
#     (0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
#     (0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
#     (0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
#     (0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
#     (0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
#     (0), 1, 4, 7, 10, 12, 15, 16, 19, (22)
#
# (The charging outlet and your device's built-in adapter are shown in 
# parentheses.) Given the adapters from the first example, the total number 
# of arrangements that connect the charging outlet to your device is 8.
#
# The second example above (the one that starts with 28, 33, 18) has many 
# arrangements. Here are a few:
#
#     (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
#     32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, (52)
#
#     (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
#     32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 49, (52)
#
#     (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
#     32, 33, 34, 35, 38, 39, 42, 45, 46, 48, 49, (52)
#
#     (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
#     32, 33, 34, 35, 38, 39, 42, 45, 46, 49, (52)
#
#     (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
#     32, 33, 34, 35, 38, 39, 42, 45, 47, 48, 49, (52)
#
#     (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
#     46, 48, 49, (52)
#
#     (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
#     46, 49, (52)
#
#     (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
#     47, 48, 49, (52)
#
#     (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
#     47, 49, (52)
#
#     (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
#     48, 49, (52)
#
# In total, this set of adapters can connect the charging outlet to your
# device in 19208 distinct arrangements.
#
# You glance back down at your bag and try to remember why you brought so 
# many adapters; there must be more than a trillion valid ways to arrange 
# them! Surely, there must be an efficient way to count the arrangements.
#
# What is the total number of distinct ways you can arrange the adapters to
# connect the charging outlet to your device?
# -----------------------------------------------------------------------------------

adapter_array = []
my_file = open('input.txt')
content = my_file.read()

adapter_array = content.split("\n")
t = 0
while t < len(adapter_array):
  adapter_array[t] = int(adapter_array[t])
  t = t + 1 

adapter_array.sort()
my_adapter = adapter_array[len(adapter_array) - 1] + 3
adapter_array.append(my_adapter)

print(adapter_array)
i = 0
curr_volt = 0
volt_change = [ 0, 0, 0, 0]
change_array = []

#all the 1,1,1,1, is exponential 2^thing between 3s
ones = False
while i < len(adapter_array):
  change_array.append(adapter_array[i] - curr_volt)
  curr_volt = adapter_array[i]
  i = i + 1

print(change_array)
ones = 1
poss = 1
i = 0
start = True
to_count = [1, 2, 4, 7, 6]
add_poss = 0

while i < len(change_array):
  if change_array[i] == 1:
    ones = ones + 1
  else:
    print("ones: ", ones)
    if ones > 2:
      ones = ones - 2
      while ones > 0:
        while ones > 3:
          add_poss = add_poss + 6
          ones = ones - 1
        if ones == 3:
          add_poss = add_poss + 7
          ones = 0
        elif ones == 2:
          add_poss = add_poss + 4
          ones = 0
        elif ones == 1:
          add_poss = add_poss + 2
          ones = 0
        elif ones == 0:
          add_poss = add_poss + 1
          ones = 0
      if add_poss == 0:
        add_poss = 1
      print("add_poss: ", add_poss)
      poss = poss * add_poss
      print("poss: ", poss)
      add_poss = 0
      ones = 1
    else:
      ones = 1
  i = i + 1

print(poss)
