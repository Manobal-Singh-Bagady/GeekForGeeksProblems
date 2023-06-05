#User function Template for python3

class Solution:
    def printDiamond(self, N):
        for i in range(1,N+1):
            print(" "*(N-i)+'* '*i)
        for i in range(N, 0, -1):
            print(" "*(N-i)+'* '*i)
            
            


# ----*
# ---* *
# --* * *
# -* * * *
# * * * * *
# * * * * *
# -* * * *
# --* * *
# --* *
# ---*


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printDiamond(N)
# } Driver Code Ends