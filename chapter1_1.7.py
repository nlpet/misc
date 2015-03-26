'''

Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column is set to 0.


1 2 3
4 0 6
7 8 9

'''




matrix = [[0,2,3],[4,5,6],[7,8,9]]

locs = set()


def print_matrix(matrix):
  print '-'*20
  for i in range(len(matrix)):
    print ' '.join([str(x) for x in matrix[i]])
    
    
print_matrix(matrix)

for i in range(len(matrix)):
  for j in range(len(matrix[0])):
    if matrix[i][j] == 0:
      locs.add((i,j))
      
for loc in locs:
  row = loc[0], 0
  col = 0, loc[1]
  
  for c in range(len(matrix[0])):
    matrix[row[0]][c] = 0
    
  for r in range(len(matrix)):
    matrix[r][col[1]] = 0
    

print_matrix(matrix)