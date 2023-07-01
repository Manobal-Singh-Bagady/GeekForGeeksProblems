#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		ans = arr[0]
		p = 1
		s = 1
		for i in range(n):
		    p = 1 if p==0 else p
		    s = 1 if s==0 else s
		    p*=arr[i]
		    s*=arr[-(i+1)]
		    ans = max((ans,p,s))
	    return ans
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends