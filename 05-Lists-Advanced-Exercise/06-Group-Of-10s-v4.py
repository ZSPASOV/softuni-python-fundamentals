import math

nums = list(map(int, input().split(', ')))

max_num = max(nums)
number_of_groups = math.ceil(max_num / 10)

for i in range(1, number_of_groups + 1):
    upper = i * 10
    lower = upper - 10

    current_range_two = [n for n in nums if lower < n <= upper]

    print(f"Group of {i * 10}'s: {current_range_two}")