class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Eratosthene's method O(n log log n)
        ret = 0
        primes = [True] * n
        for i in range(2,n):
            if primes[i]:
                ret += 1
                for j in range(2, (n - 1) // i + 1): # i * j < n
                    primes[i*j] = False
        return ret