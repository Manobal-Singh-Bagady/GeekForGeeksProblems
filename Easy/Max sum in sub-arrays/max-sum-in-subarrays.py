#User function Template for python3

class Solution:
    def pairWithMaxSum(self, arr, N):
        mx = 0
        for i in range(N-1):
            mx = max(mx,(arr[i]+arr[i+1]))
        return mx
            
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.pairWithMaxSum(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends