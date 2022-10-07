# -----------------------------------------------------------------------------------
# --- Part Two ---
# After some careful analysis, you believe that exactly one instruction 
# is corrupted.
#
# Somewhere in the program, either a jmp is supposed to be a nop, or a nop is
# supposed to be a jmp. (No acc instructions were harmed in the corruption of 
# this boot code.)
#
# The program is supposed to terminate by attempting to execute an
# instruction immediately after the last instruction in the file. By changing 
# exactly one jmp or nop, you can repair the boot code and make it terminate
# correctly.
#
# For example, consider the same program from above:
#
#     nop +0
#     acc +1
#     jmp +4
#     acc +3
#     jmp -3
#     acc -99
#     acc +1
#     jmp -4
#     acc +6
#
# If you change the first instruction from nop +0 to jmp +0, it would create 
# a single-instruction infinite loop, never leaving that instruction. If you 
# change almost any of the jmp instructions, the program will still 
# eventually find another jmp instruction and loop forever.
#
# However, if you change the second-to-last instruction (from jmp -4 to 
# nop -4), the program terminates! The instructions are visited in this 
# order:
#
#     nop +0  | 1
#     acc +1  | 2
#     jmp +4  | 3
#     acc +3  |
#     jmp -3  |
#     acc -99 |
#     acc +1  | 4
#     nop -4  | 5
#     acc +6  | 6
#
# After the last instruction (acc +6), the program terminates by attempting 
# to run the instruction below the last instruction in the file. With this 
# change, after the program terminates, the accumulator contains the value 8 
# (acc +1, acc +1, acc +6).
#
# Fix the program so that it terminates normally by changing exactly one jmp
# (to nop) or nop (to jmp). What is the value of the accumulator after the
# program terminates?
# -----------------------------------------------------------------------------------


code_array = []
my_file = open('input.txt')
content = my_file.read()

code_array = content.split("\n")
visited = [False]*len(code_array)
i = 0
remem_poss = 0
change = "text"
answer = 0

def rep_check(position, da_code):
  visited = [False]*len(code_array)
  repeated = False
  accum = 0
  j = 0
  while repeated == False:
    if len(code_array) == j:
      repeated = True
      return True, accum
    elif visited[j] == True:
      repeated = True
      return False, accum
    else:
      visited[j] = True
      if position == j:
        curr_code = [da_code, code_array[j][4:5], code_array[j][5:]]
      else:
        curr_code = [code_array[j][:3], code_array[j][4:5], code_array[j][5:]]
      if curr_code[0] == "acc":
        if curr_code[1] == "+":
          accum = accum + int(curr_code[2])
          j = j + 1
        else:
          accum = accum - int(curr_code[2])
          j = j + 1
      elif curr_code[0] == "jmp":
        if curr_code[1] == "+":
          j = j + int(curr_code[2])
        else:
          j = j - int(curr_code[2])
      else:
        j = j + 1

found = False
while found == False:
  if code_array[remem_poss][:3] == "jmp":
    change = "nop"
    found, answer = rep_check(remem_poss, change)
    remem_poss = remem_poss + 1
  elif code_array[remem_poss][:3] == "nop":
    change = "jmp"
    found, answer = rep_check(remem_poss, change)
    remem_poss = remem_poss + 1
  else:
    remem_poss = remem_poss + 1  
  if found == True:
    print(answer)
