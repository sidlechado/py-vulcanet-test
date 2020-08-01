# Mussum recently bought a pack of Cacildis, which each can has an specific
# height. The cans in the pack are stored sequentially. The height of each can is
# a number in a permutation from 1 to n. A permutation of 1 to n is a sequence
# of n numbers in which each number from 1 to n occurs exactly once.
# In this pack of Cacildis, Mussum wants to now if there is a can that is taller
# than any can on its left and right. That is: given a permutation p1, p2, ..., pn, if
# there are pi
# , pj , pk such that i < j < k and pi < pj and pj > pk.

print("Welcom to the Mussun Cacildis!")
print("The instructions are as follows:")
print("1. The number of games can be between 1 and 200.")
print("2. Each pack can have between 3 and 100 Cans.")

while True:
  nr_test_cases = int(input("Enter the number of games: "))
  if nr_test_cases > 0 and nr_test_cases < 201:
    break
  else:
    print('Invalid number of tests. It should be between 1 and 200.\n')


heights = [int(heights) for heights in input().split()] 

i = 5
while i > 0:
  print(i)
  i = i - 1
  

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