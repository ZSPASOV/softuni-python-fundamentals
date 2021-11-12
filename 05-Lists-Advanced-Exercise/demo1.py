def modify_num(x):
    res = x
    if x % 2 == 0:
        res = x * 10
    return res


nums = [1, 2, 3, 4, 5, 6]

result = [modify_num(x) for x in nums]

print(nums)
print(result)