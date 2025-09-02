class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = 0
        for i in range(1, n):
            n -= i
            k += 1
            print(n, k, i)
            if n == 0:
                return k
            elif n < 0:
                return k - 1
