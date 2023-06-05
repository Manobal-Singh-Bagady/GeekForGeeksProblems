#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range(2*N-1):
            for j in range(2*N-1):
                left = j
                top = i
                right = 2*(N-1)-j
                bottom = 2*(N-1)-i
                print(N-min(left, right, top, bottom), end=' ')
            print()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends