hapiness_indexes = [int(n) for n in input().split(' ')]
improvement_factor = int(input())

factored_happiness_indexes = [v * improvement_factor for v in hapiness_indexes]
average_happiness = sum(factored_happiness_indexes) / len(factored_happiness_indexes)
happy_values = list(filter(lambda n: n >= average_happiness, factored_happiness_indexes))
happy_count = len(happy_values)
total_count = len(hapiness_indexes)

if happy_count >=(len(hapiness_indexes) / 2):
    print(f'Score: {happy_count}/{total_count}. Employees are happy!')
else:
    print(f'Score: {happy_count}/{total_count}. Employees are not happy!')