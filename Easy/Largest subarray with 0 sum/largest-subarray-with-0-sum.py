#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        maxln = 0
        sum = 0
        mp = {}
        for i,x in enumerate(arr):
            sum+=x
            if sum==0:
                maxln = max(maxln,i+1)
            if sum not in mp:
                mp[sum]=i
            else:
                maxln = max(maxln,i-mp[sum])
        return maxln


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends