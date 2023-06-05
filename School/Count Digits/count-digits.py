#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        num = N
        count=0
        while num>0:
            temp = num%10
            if temp!=0 and N%temp == 0:
                count+=1
            num//=10
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends