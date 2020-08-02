# print("Welcom to the Mussun Cacildis!")
# print("The instructions are as follows:")
# print("1. The number of games can be between 1 and 200.")
# print("2. Each pack can have between 3 and 100 Cans.")

# while True:
#   nr_test_cases = int(input("Enter the number of games: "))
#   if nr_test_cases > 0 and nr_test_cases < 201:
#     break
#   else:
#     print('Invalid number of tests. It should be between 1 and 200.\n')

def verify_right(right_part_of_list, height_being_verified, current_index):
  i = 0
  controller = [False, []]
  while i < len(right_part_of_list):
    if height_being_verified > right_part_of_list[i]:
      controller[0] = True
      controller[1] = controller[1] + (i + current_index)
    i += 1
  return controller

## VERIFY AND DRAW
def verify_left(left_part_of_list, height_being_verified, current_index):
  i = 0
  controller = [False, []]
  while i < len(left_part_of_list):
    if height_being_verified > left_part_of_list[i]:
      controller[0] = True
      controller[1] = controller[1] + (i + current_index)
    i += 1
  return controller

lenght = int(input('lenght of permutation'))
heights = [int(heights) for heights in input('heights').split()] 
empty_solution_list = []
i = 0
while i < lenght:
  left_verification= [] #Will return on index 0 a true or false, and on index 1, all the indexes
  right_verification = []
  #Quebrar a verificacao em direita e esquerda, se é o primeiro ou ultimo, n verifica
  if i != 0 or i != (lenght - 1):
    left_verification= verify_left(heights[0:i-1], heights[i], i)
    right_verification = verify_right(heights[i+1:lenght-1], heights[i], i)
  print(heights[i])
  i += 1
  

# for can in heights:
#     print(can)
# nr_cans_pack = int(input("Enter the number of cans in the pack: "))


# each pack has Y cans stored sequentially, array like
# each can has a height
# each height is part of a permutation from 1 to n
# have to verify if there is a can in the middle of two (can be more than two) that has a higher height than the ones on the left and the ones on the right, so it should be the highest


# nr_tests_cases = 3
# 4                     YES
# 2 1 4 3               2 3 4 

# 6                     YES
# 4 6 1 2 5 3           3 5 6

# 5                     NO
# 5 3 1 2 4
