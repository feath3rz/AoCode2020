# -----------------------------------------------------------------------------------
# --- Part Two ---
# You manage to answer the child's questions and they finish part 1 of their 
# homework, but get stuck when they reach the next section: advanced math.
#
# Now, addition and multiplication have different precedence levels, but 
# they're not the ones you're familiar with. Instead, addition is evaluated 
# before multiplication.
#
# For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are 
# now as follows:
#
#     1 + 2 * 3 + 4 * 5 + 6
#       3   * 3 + 4 * 5 + 6
#       3   *   7   * 5 + 6
#       3   *   7   *  11
#          21       *  11
#              231
#
# Here are the other examples from above:
#
#   - 1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
#   - 2 * 3 + (4 * 5) becomes 46.
#   - 5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
#   - 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
#   - ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.
#
# What do you get if you add up the results of evaluating the homework
# problems using these new rules?
# -----------------------------------------------------------------------------------

problems_array = []
my_file = open('input.txt')
content = my_file.read()

problems_array = content.split("\n")
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def math_it(the_array):
  curr_num = 0
  z = 0
  while z < len(the_array):
    if the_array[z] == "(":
      y = z + 1
      end_para = 0
      add_para = 0
      while y < len(the_array):
        if the_array[y] == "(":
          add_para = add_para + 1
        elif the_array[y] == ")":
          if add_para == 0:
            end_para = y
            y = len(the_array)
          else:
            add_para = add_para - 1
        y = y + 1
      
      #send it to recursive
      curr_num = math_it(the_array[z + 1:end_para])
      while end_para >= z:
        the_array.pop(z)
        end_para = end_para - 1

      the_array.insert(z, curr_num)
    z = z + 1

  z = 0
  while z < len(the_array):
    if the_array[z] == '+':
      curr_num = the_array[z - 1] + the_array[z + 1]
      the_array.pop(z - 1)
      the_array.pop(z - 1)
      the_array.pop(z - 1)
      the_array.insert(z - 1, curr_num)
    else:
      z = z + 1

  z = 0
  while z < len(the_array):
    if the_array[z] == '*':
      curr_num = the_array[z - 1] * the_array[z + 1]
      the_array.pop(z - 1)
      the_array.pop(z - 1)
      the_array.pop(z - 1)
      the_array.insert(z - 1, curr_num)
    else:
      z = z + 1
    
  return the_array[0]
    
a = 0
total = 0
while a < len(problems_array):
  math_array = list(problems_array[a])

  while ' ' in math_array:
    math_array.remove(' ')

  b = 0
  while b < len(math_array):
    if math_array[b] in number:
      math_array[b] = int(math_array[b])
    b = b + 1
  result = math_it(math_array)
  total = total + result
  a = a + 1

print(total)
