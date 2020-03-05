'''
Given an image represented by an N x N matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

 

Example 1:

Given matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

Rotate the matrix in place. It becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:

Given matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

Rotate the matrix in place. It becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]


执行用时 :20 ms, 在所有 Python 提交中击败了78.79% 的用户
内存消耗 :11.7 MB, 在所有 Python 提交中击败了100.00%的用户
'''

class Solution(object):
    def rotate(self, matrix):
        length = len(matrix)
        
        for i in range(0, length):
            bian = length-1-i
            if (i < length-1-i):
                for j in range(i, length-i-1):
                    k = length-1-i-i
                    
                    if i == j:
                        m1 = matrix[i][j]
                        m2 = matrix[j][bian]
                        m3 = matrix[bian][bian]
                        m4 = matrix[bian][j]

                        matrix[i][j] = m4
                        matrix[j][bian] = m1
                        matrix[bian][bian] = m2
                        matrix[bian][i] = m3
                        
                    
                    else:
                        m1 = matrix[i][j]
                        m2 = matrix[j][bian]
                        m3 = matrix[bian][length-1-j]
                        m4 = matrix[length-1-j][i]

                        matrix[i][j] = m4
                        matrix[j][bian] = m1
                        matrix[bian][length-1-j] = m2
                        matrix[length-1-j][i] = m3
                    
