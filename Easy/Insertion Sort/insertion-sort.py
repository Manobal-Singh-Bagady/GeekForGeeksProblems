#Sort the array using insertion sort

class Solution:
    def insert(self, alist, index, n):
        for i in range(index, -1, -1):
            if alist[i+1]>alist[i]:
                break
            alist[i],alist[i+1] = alist[i+1], alist[i]
            
                
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        for i in range(n-1):
                self.insert(alist, i, n)
                


#{ 
 # Driver Code Starts
if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
# } Driver Code Ends