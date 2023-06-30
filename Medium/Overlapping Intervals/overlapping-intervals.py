class Solution:
	def overlappedInterval(self, Intervals):
	    ans = []
		Intervals.sort()
		s = Intervals[0][0]
		e = Intervals[0][1]
		
		for x,y in Intervals:
		    if x<=e:
		        e = max(e,y)
		    else:
		        ans.append([s,e])
		        s = x
		        e = y
		ans.append([s,e])
	    return ans
		        


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends