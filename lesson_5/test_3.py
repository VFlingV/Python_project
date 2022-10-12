import random
def find_missing(t):
    num = list(map(int, t.split(' ')))
    result = None
    for i in range(1, len(num)):
        if num[i] - 1 != num[i - 1]:
            result = num[i] - 1
    return result


def inc(nums):
    result = nums[:1]
    for i in range(1, len(nums)):
        if nums[i] > result[-1]:
            result.append(nums[i])
    return result


num = [1, 2, 1, 4, 1, 10, 2, 6, 9]
print(inc(num))
"""
return range(x, x * n + 1, x)
"""

f = random.randint(1, 28)
print(f)