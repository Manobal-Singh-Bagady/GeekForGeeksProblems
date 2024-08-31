//{ Driver Code Starts
// Initial Template for Java
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            long N = sc.nextLong();

            Solution ob = new Solution();
            ArrayList<Long> ans = ob.factorialNumbers(N);
            for (long num : ans) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }
}

// } Driver Code Ends


// User function Template for Java
class Solution {
    int cnt = 1;
    long fac = 1;
    ArrayList<Long> list = new ArrayList<>();
    ArrayList<Long> factorialNumbers(long n) {
        fac*=cnt;
        if(fac>n) {
            return list;
        }
        
        list.add(fac);
        cnt++;
        
        factorialNumbers(n);
        return list;
    }
}