def calcSum(n):
    result = 0
    while n:
        result += (n % 10) ** 2
        n //= 10
    return result

class Solution:
    def isHappy(self, n: int) -> bool:
        cycle_set = set()
        n = calcSum(n)
        while n != 1:
            n = calcSum(n)
            print(n)
            if n in cycle_set:
                return False
            cycle_set.add(n)
        return True
