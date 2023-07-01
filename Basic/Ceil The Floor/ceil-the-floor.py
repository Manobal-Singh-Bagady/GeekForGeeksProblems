#User function Template for python3




def getFloorAndCeil(arr, n, x):
    floor = -1
    ceil = -1
    for i in arr:
        if i>=x:
            ceil = i if ceil==-1 else min(ceil, i)
        if i<=x:
            floor = max(floor, i)
    return (floor, ceil)
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))

        ans = getFloorAndCeil(arr, n, x)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# } Driver Code Ends