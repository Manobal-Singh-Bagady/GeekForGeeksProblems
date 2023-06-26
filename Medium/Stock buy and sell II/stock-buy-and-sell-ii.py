#User function Template for python3



def stockBuySell(price, n):
    buy=0
    sell=0
    i = 0
    flag = True
    while i<n:
        while(i<n-1 and price[i]>=price[i+1]):
            i+=1
        buy = i
        
        while i<n-1 and price[i]<=price[i+1]:
            i+=1
        sell = i
        
        if sell-buy>0:
            print("("+str(buy)+" "+str(sell)+")",end=" ")
            flag = False
        i+=1
        
    if flag:
        print("No Profit",end=" ")
        
    print()
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        price=list(map(int, input().split()))
        stockBuySell(price, n)
# } Driver Code Ends