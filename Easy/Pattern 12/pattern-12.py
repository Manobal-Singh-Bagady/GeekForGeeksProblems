#User function Template for python3

class Solution:
    def printTriangle(self, N):
        start = 4*(N-1)
        for i in range(1,N+1):
            for j in range(1,i+1):
                print(j, end=" ")
                
            print(" "*start, end="")
            start-=4
            
            for j in range(i,0,-1):
                print(j, end=" ")
            print()
                
# 1 ----------------1
# 1 2 ------------2 1
# 1 2 3 --------3 2 1
# 1 2 3 4 ----4 3 2 1
# 1 2 3 4 5 5 4 3 2 1


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