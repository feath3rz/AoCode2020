# -----------------------------------------------------------------------------------
# https://adventofcode.com/2020/day/18
# 
# --- Day 18: Operation Order ---
# As you look out the window and notice a heavily-forested continent slowly
# appear over the horizon, you are interrupted by the child sitting next to
# you. They're curious if you could help them with their math homework.
#
# Unfortunately, it seems like this "math" follows different rules than you 
# remember.
#
# The homework (your puzzle input) consists of a series of expressions that 
# consist of addition (+), multiplication (*), and parentheses ((...)). Just 
# like normal math, parentheses indicate that the expression inside must be 
# evaluated before it can be used by the surrounding expression. Addition 
# still finds the sum of the numbers on both sides of the operator, and 
# multiplication still finds the product.
#
# However, the rules of operator precedence have changed. Rather than
# evaluating multiplication before addition, the operators have the same
# precedence, and are evaluated left-to-right regardless of the order in 
# which they appear.
#
# For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are 
# as follows:
#
#     1 + 2 * 3 + 4 * 5 + 6
#       3   * 3 + 4 * 5 + 6
#           9   + 4 * 5 + 6
#              13   * 5 + 6
#                  65   + 6
#                      71
#
# Parentheses can override this order; for example, here is what happens if 
# parentheses are added to form 1 + (2 * 3) + (4 * (5 + 6)):
#
#     1 + (2 * 3) + (4 * (5 + 6))
#     1 +    6    + (4 * (5 + 6))
#          7      + (4 * (5 + 6))
#          7      + (4 *   11   )
#          7      +     44
#                 51
#
# Here are a few more examples:
#
#   - 2 * 3 + (4 * 5) becomes 26.
#   - 5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
#   - 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
#   - ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.
#
# Before you can help with the homework, you need to understand it yourself.
# Evaluate the expression on each line of the homework; what is the sum of 
# the resulting values?
# -----------------------------------------------------------------------------------

problems_array = []
my_file = open('input.txt')
content = my_file.read()

problems_array = content.split("\n")
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def math_it(the_array):
  z = 0
  curr_total = 0
  if the_array[z] in number:
    curr_total = curr_total + int(the_array[z])
    z = 1
  add_it = False
  multiply = False
  value = False
  while z < len(the_array):
    if the_array[z] == "(":
      #find end
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
      value = True
      z = end_para
    elif the_array[z] in number:
      curr_num = int(the_array[z])
      value = True
    elif the_array[z] == "+":
      add_it = True
    elif the_array[z] == "*":
      multiply = True
    
    if value == True:
      if add_it == True:
        curr_total = curr_total + curr_num
        add_it = False
        value = False
      if multiply == True:
        curr_total = curr_total * curr_num
        multiply = False
        value = False
      if curr_total == 0:
        curr_total = curr_num
        value = False
    z = z + 1
  
  return curr_total
    
a = 0
total = 0
while a < len(problems_array):
  math_array = list(problems_array[a])

  while ' ' in math_array:
    math_array.remove(' ')
  result = math_it(math_array)
  total = total + result
  a = a + 1

print(total)
