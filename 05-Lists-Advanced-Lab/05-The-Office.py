hapiness = [int(n) for n in input().split(' ')]
factor = int(input())
modified_happiness = [n * factor for n in hapiness]
more_than_average = [n for n in modified_happiness if n >= sum(modified_happiness) / len(modified_happiness)]

if len(more_than_average) / len(modified_happiness) >= 0.5:
    print(f'Score: {len(more_than_average)}/{len(modified_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(more_than_average)}/{len(modified_happiness)}. Employees are not happy!')
