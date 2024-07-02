#!/usr/bin/python3
"""Generate Strong"""


def isWinner(x, nums):
    """andromidia"""
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

        _prime = prime.copy()
        for d in range(2, n+1):
            if not prime[d]:
                _prime.pop(d)

        rounds.append(len(_prime) % 2)

    if rounds.count(0) > rounds.count(1):
        return "Ben"
    else:
        return "Maria"
