#User function Template for python3
class Solution:

	def count(self,arr, n, x):
		l = 0
		r = n-1
		while l<=r:
		    mid = (l+r)//2
		    if arr[mid]>=x:
		        r = mid-1
		    else:
		        l = mid+1
        if l == n or arr[l]!=x:
            return 0
        else: f = l
        
        l = 0
        r = n-1
        while l<=r:
            mid = (l+r)//2
            if arr[mid]>x:
                r = mid-1
            else:
                l = mid+1
        return (l-f)


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends