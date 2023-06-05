#User function Template for python3

class Solution:
    def printTriangle(self, N):
        
        for i in range(1, N+1):
            print(" "*(N-i), end='')
           
            for j in range(65, 65+i):
                print(chr(j), end="")
            for j in range(63+i, 64, -1):
                print(chr(j), end='')
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