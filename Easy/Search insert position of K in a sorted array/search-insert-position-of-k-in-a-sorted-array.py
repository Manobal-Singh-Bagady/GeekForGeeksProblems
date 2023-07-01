#User function Template for python3

class Solution:
    def searchInsertK(self, Arr, N, k):
        l = 0
        h = N-1
        while l<=h:
            mid = (l+h)//2
            if Arr[mid]>k:
                h = mid-1
            elif Arr[mid]<k:
                l = mid+1
            else:
                return mid
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.searchInsertK(Arr, N, k))
# } Driver Code Ends