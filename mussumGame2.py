import sys
import numpy as np
#region variables
data_storage = []
output = []
nr_tests = 0
iterator_tests = 0
iterator_rows = 0
iterator_matrix = 0
# global column_indexes
# global row_indexes
column_indexes = []
row_indexes = []

#endregion

#region functions

def print_output(output):
  for test_result in output:
    print(test_result)
  return

def checking_filled_entries(matrix):
  iterator_column = 0
  iterator_row = 0

  while iterator_row < len(matrix[0]):
    while iterator_column < len(matrix):
      if matrix[iterator_row][iterator_column] == 1:
        column_indexes.append(iterator_column)
        row_indexes.append(iterator_row)
      
      iterator_column += 1
    iterator_row += 1

def unique_indexes(list_of_indexes):
  np_indexes = np.array(list_of_indexes)

  return np.unique(np_indexes)

def delete_rows(matrix, unique_row_indexes):
  index = 0
  while index < len(unique_row_indexes):
    matrix = np.delete(matrix, unique_row_indexes[index], 0)
    index += 1

  return matrix

def delete_columns(matrix, unique_column_indexes):
  index = 0
  while index < len(unique_column_indexes):
    matrix = np.delete(matrix, unique_column_indexes[index], 0)
    if len(matrix) == 1:
      return False
    index += 1

  return matrix

def game(matrix):
  game = True
  nr_of_rounds = 1
  while game == True:
    if len(matrix) >= 1 and len(matrix[0]) >= 1:
      nr_of_rounds += 1
      matrix = delete_rows(matrix, [0])
      matrix = delete_columns(matrix, [0])
    else:
      game = False
  return nr_of_rounds

#Getting number of test cases
nr_tests = int(input())
if nr_tests < 1 or nr_tests > 50:
  print('Invalid number of tests.')
  print('Please, choose between 1 and 200.')
  sys.exit()

#Getting matrixes for each test case
while iterator_tests < nr_tests:
  #Geting nr of rows and columns for the matrix
  matrix_definition = [int(matrix_definition) for matrix_definition in input().split()]
  nr_rows = matrix_definition[0]
  nr_columns = matrix_definition[1]
  iterator_rows = 0

  #Used for getting all the row entries in a matrix
  list_iterator_for_rows = []

  #Satisfying the minimum and maximum number of columns/rows
  if nr_rows < 1 or nr_rows > 50:
    print('Invalid number of rows.')
    print('Please, choose between 1 and 50.')
    sys.exit()

  if nr_columns < 1 or nr_columns > 50:
    print('Invalid number of columns.')
    print('Please, choose between 1 and 50.')
    sys.exit()

4 - Construir uma arquitetura cliente servidor em python para gerenciamento de filas.

5 - Entrevista via hangouts e então uma proposta será formalmente feita.
  while iterator_rows < nr_rows:
    matrix_row_input = [int(matrix_row_input) for matrix_row_input in input().split()]
    list_iterator_for_rows.append(matrix_row_input)
    iterator_rows += 1

  data_storage.append(list_iterator_for_rows)

  iterator_tests += 1

#Iterating throguh each test case and testing the matrix
iterator_tests = 0
for test in data_storage:
  matrix = np.array(data_storage[iterator_tests])

  checking_filled_entries(matrix)
  print(column_indexes)
  print(row_indexes)
  unique_column_indexes = unique_indexes(column_indexes)
  unique_row_indexes = unique_indexes(row_indexes)

  matrix = delete_rows(matrix, unique_row_indexes)
  matrix = delete_columns(matrix, unique_column_indexes)
  print(matrix)
  nr_of_rounds = game(matrix)

  if (nr_of_rounds % 2) == 0:
    output.append('Ashish')
  else:
    output.append('Vivek')

  iterator_tests += 1

print_output(output)