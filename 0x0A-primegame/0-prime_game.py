#!/usr/bin/python3
"""Generate Strong"""


def isWinner(x, nums):
    """andromidia"""
    
    if x > len(nums):
        return None

    rounds = []
    for _1 in range(x):
        n = nums[_1]
        prime = [True for i in range(n + 1)]
        p = 2

        while (p * p <= n):
            if prime[p]:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1

        prime_count = sum(1 for _ in range(2, n+1) if prime[_])

        rounds.append(prime_count % 2)

    if rounds.count(0) > rounds.count(1):
        return "Ben"
    elif rounds.count(1) > rounds.count(0):
        return "Maria"
    else:
        return None
