#User function Template for python3

class Solution:
    def MakeZeros(self, matrix: list):
        ans = [i.copy() for i in matrix]
        for i, x in enumerate(matrix):
            for j, y in enumerate(x):
                if y == 0:
                    # print(i, j)
                    A = B = C = D = 0
                    if j != 0:
                        A = matrix[i][j - 1]
                        ans[i][j - 1] = 0
                    if j != len(x) - 1:
                        B = matrix[i][j + 1]
                        ans[i][j + 1] = 0
                    if i != 0:
                        C = matrix[i - 1][j]
                        ans[i - 1][j] = 0
                    if i != len(matrix) - 1:
                        D = matrix[i + 1][j]
                        ans[i + 1][j] = 0
                    ans[i][j] = A + B + C + D
        matrix[:] = ans[:]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int,input().split())))
		ob = Solution()
		ob.MakeZeros(matrix)
		for i in range(n):
			for j in range(m):
				print(matrix[i][j], end = " ")
			print()
# } Driver Code Ends