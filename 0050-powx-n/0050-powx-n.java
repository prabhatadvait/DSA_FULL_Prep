class Solution {
    public double myPow(double x, int n) {
        long N = n; // This is for handling the overflow
        if(N<0){
            x = 1/x; // Taking reciprocal
            N = -N; 
        }
        return powpow(x,N);
        
    }

    private double powpow(double x,long n){
        if(n==0){
            return 1;
        }
        if(n%2==0){
            return powpow(x*x,n/2);
        }
        else{
            return x * powpow(x*x,(n-1)/2);
        }
    }
}