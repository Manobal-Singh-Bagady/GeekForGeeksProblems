#User function template for Python

class Solution:
    def bs(self, arr, l, h, k):
        if l>h:
            return -1
        mid = (l+h)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]>k:
            return self.bs(arr, l, mid-1, k)
        else:
            return self.bs(arr, mid+1, h, k)
            
	def binarysearch(self, arr, n, k):
	   return self.bs(arr, 0, n-1, k)
	   # l = 0
	   # r = n-1
	   # while l<=r:
	   #     mid = (l+r)//2
	   #     if arr[mid]>k:
	   #         r = mid-1
	   #     elif arr[mid]<k:
	   #         l = mid+1
	   #     else:
	   #         return mid
	   # return -1
		        


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends