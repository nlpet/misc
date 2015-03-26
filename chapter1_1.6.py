'''
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

1 2 3           7 4 1
4 5 6           8 5 2
7 8 9   --->    9 6 3


'''


matrix = [[1,2,3],[4,5,6],[7,8,9]]


def print_matrix(matrix):
  print '-'*20
  for i in range(len(matrix)):
    print ' '.join([str(x) for x in matrix[i]])
    

def rotate_clockwise(matrix):
  n = len(matrix[0])
  for layer in (0,n/2):
    first = layer
    last = n - 1 - layer
    for i in range(first,last):
      offset = i - first
      top = matrix[first][i] # save top
      matrix[first][i] = matrix[last-offset][first] # left -> top
      matrix[last-offset][first] = matrix[last][last-offset] # bottom -> left
      matrix[last][last-offset] = matrix[i][last] # right -> bottom
      matrix[i][last] = top # top -> right
  return matrix
      
      
  
print_matrix(matrix)
rotated_matrix = rotate_clockwise(matrix)
print_matrix(rotated_matrix)
  
