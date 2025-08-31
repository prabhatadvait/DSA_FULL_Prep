class Solution {
    public int countGoodNumbers(long n) {
        int MOD = 1_000_000_007;
        long even = (n + 1) / 2;
        long odd = n / 2;
    
        long evenPart = modPow(5, even, MOD);
        long oddPart = modPow(4, odd, MOD);

        return (int)((evenPart * oddPart) % MOD);
    }

    // private long modPow(long x, long n, int mod) {
    //     if (n == 0) {
    //         return 1;
    //     }

    //     long half = modPow((x * x) % mod, n / 2, mod);

    //     if (n % 2 == 0) {
    //         return half;
    //     } else {
    //         return (x * half) % mod;
    //     }
    // }

    private long modPow(long x, long n, int mod) {
    if (n == 0) {
        return 1;
    }
    if (n % 2 == 0) {
        return modPow((x * x) % mod, n / 2, mod);
    } else {
        return (x * modPow((x * x) % mod, (n - 1) / 2, mod)) % mod;
    }
}


}