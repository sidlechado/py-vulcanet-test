import sys
#region variables
data_storage = []
output = []
nr_tests = 0
nr_tests_iterator = 0
#endregion
#region functions
# Function will search into the right part of the list for the first index that suffices the condition
def verify_right(right_part_of_list, height_being_verified, current_index):
  i = 0
  right_verification_return = [False, -1]
  while i < len(right_part_of_list):
    if height_being_verified > right_part_of_list[i]:
      right_verification_return[0] = True
      # Relative index to the whole permutation.
      right_verification_return[1] = (i + current_index)
      break
    i += 1
  return right_verification_return

# Function will search into the left part of the list for the first index that suffices the condition
def verify_left(left_part_of_list, height_being_verified):
  i = 0
  left_verification_return = [False, -1]
  while i < len(left_part_of_list):
    if height_being_verified > left_part_of_list[i]:
      left_verification_return[0] = True
      left_verification_return[1] = i
      break
    i += 1
  return left_verification_return

def print_output(output):
  for test in output:
    print(test[0])
    if test[0] == 'YES':
      print(('{} '*len(test[1])).format(*test[1]))
  return
#endregion

#Getting number of test cases
nr_tests = int(input())
if nr_tests < 1 or nr_tests > 200:
  print('Invalid number of tests.')
  print('Please, choose between 1 and 200.')
  sys.exit()

#Getting number of cans and heights for each test case
while nr_tests_iterator < nr_tests:
  nr_cans_package = int(input())
  if nr_cans_package < 3 or nr_cans_package > 100:
    print('Invalid number of cans.')
    print('Please, choose between 3 and 100 per package.')
    sys.exit()
  heights_can_package = [int(heights_can_package) for heights_can_package in input().split()] 
  data_storage.insert(nr_tests_iterator, [nr_cans_package, heights_can_package])
  nr_tests_iterator += 1

#Testing each input
nr_tests_iterator = 0
while nr_tests_iterator < nr_tests:
  lenght = data_storage[nr_tests_iterator][0]
  heights = data_storage[nr_tests_iterator][1]
  output.insert(nr_tests_iterator, ['NO', -1])
  
  i = 0
  while i < lenght:
    # List of 2 positions
    # List[0] -> Yes or No
    # List[1] -> First index that suffices the condition
    left_verification= []
    right_verification = []

    #Wont verify first and last position of permutation
    if i != 0:
      if i != (lenght - 1):
        #Params
        #Left side of list til number being verified, number being verified
        left_verification = verify_left(heights[0:(i)], heights[i])

        #Only will verify right part of list if left part verification returns true.
        if left_verification[0]:
          #Params
          #Right side of list after number being verified, number being verified, current index of permutation
          right_verification = verify_right(heights[(-lenght+i+1):], heights[i], (i+1))

        # Will rewrite currently output if theres a triad of indexes that satisfy games condition
        if left_verification[0] and right_verification[0]:
          output[nr_tests_iterator][0] = 'YES'
          output[nr_tests_iterator][1] = [left_verification[1]+1, (i+1), (right_verification[1]+1)]
    i += 1
  nr_tests_iterator += 1

print_output(output)