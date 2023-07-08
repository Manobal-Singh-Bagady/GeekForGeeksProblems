#User function Template for python3

class Solution:
    def Search(self, n, arr, k):
        l = 0
        r = n-1
        while l<=r:
            mid = (l+r)//2
            if arr[mid]==k:
                return 1
            if arr[l]==arr[mid] and arr[mid]==arr[r]:
                l += 1
                r -= 1
                continue
            if arr[l]<=arr[mid]:
                if arr[l]<=k<=arr[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if arr[mid]<=k<=arr[r]:
                    l = mid+1
                else:
                    r = mid-1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        ans = ob.Search(n, arr, k)
        print(ans)
        tc -= 1
# } Driver Code Ends