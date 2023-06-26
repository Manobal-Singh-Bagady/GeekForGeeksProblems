#User function Template for python3

class Solution:
    def rearrange(self, arr, n):
        pos = []
        neg = []
        for i in arr:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
        for i in range(n):
            if i % 2 == 0:
                if pos:
                    arr[i] = pos.pop(0)
                else:
                    arr[i] = neg.pop(0)
            else:
                if neg:
                    arr[i] = neg.pop(0)
                else:
                    arr[i] = pos.pop(0)
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends