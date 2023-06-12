class Solution:
    def leftRotate(self, arr, k, n):
        k %= n
        temp = arr[:k]
        for i in range(k,n):
            arr[i-k] = arr[i]
        x = n-k
        for i in range(k):
            arr[x] = temp[i]
            x+=1
            


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a = list(map(int,input().split()))
        ob = Solution()
        ob.leftRotate(a,k,n)
        print(*a)
# } Driver Code Ends