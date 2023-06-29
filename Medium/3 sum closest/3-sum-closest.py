#User function Template for python3
import sys
class Solution:
    def closest3Sum(self, A, N, X):
        ans = sys.maxsize
        A.sort()
        for i in range(N):
            if i>0 and A[i]==A[i-1]:
                continue
            j = i+1
            k = N-1
            while j<k:
                sum = A[i]+A[j]+A[k]
                
                if abs(X-sum)<abs(X-ans):
                    ans = sum
                if sum<X:
                    j+=1
                elif sum>X:
                    k-=1
                else:
                    return sum
        return ans


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
        X = int(input())
        ob = Solution()
        print(ob.closest3Sum(Arr, N, X))
# } Driver Code Ends