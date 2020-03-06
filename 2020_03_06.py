'''
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

执行用时 :24 ms, 在所有 Python 提交中击败了100.00% 的用户
内存消耗 :12.5 MB, 在所有 Python 提交中击败了100.00%的用户
'''

class Solution(object):
    def setZeroes(self, matrix):
        M = len(matrix)
        N = len(matrix[0])
        iset = []
        jset = []
        for i in range(0, M):
            for j in range(0, N):
                if matrix[i][j] == 0:
                    iset.append(i)
                    jset.append(j)
        
        for index in iset:
            for j in range(0, N):
                matrix[index][j] = 0
        
        for jndex in jset:
            for i in range(0, M):
                matrix[i][jndex] = 0
