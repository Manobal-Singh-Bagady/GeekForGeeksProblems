#User function Template for python3

class Solution:
    def factorialNumbers(self, N):
        ans = []
    	def fact(n, fac, i):
    	    i+=1
    	    if fac>n:
    	        return
    	    ans.append(fac)
    	    fact(n, fac*i, i)
    	fact(N,1,1)
    	return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()
        
# } Driver Code Ends