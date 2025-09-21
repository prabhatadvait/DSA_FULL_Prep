class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0  # there are no primes less than 2

        # Step 1: Assume all numbers < n are prime
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

        # Step 2: Only need to check up to sqrt(n)
        limit = int(n ** 0.5)
        for i in range(2, limit + 1):
            if is_prime[i]:
                # Step 3: Mark multiples of i as not prime
                for j in range(i * i, n, i):  # start from i^2
                    is_prime[j] = False

        # Step 4: Count how many numbers are still prime
        return sum(is_prime)
