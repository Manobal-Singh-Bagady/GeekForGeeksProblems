#User function Template for python3


def find(arr, n, x):
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] >= x:
            r = mid - 1
        else:
            l = mid + 1
    if l == n or arr[l] != x:
        return (-1, -1)
    else:
        first = l
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    last = l - 1
    return (first, last)
    



#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends