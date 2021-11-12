n = int(input())
positive_numbers = []
negative_numbers = []

for i in range(n):
    number_for_list = int(input())
    if number_for_list >= 0:
        positive_numbers.append(number_for_list)
    else:
        negative_numbers.append(number_for_list)

count_positives = len(positive_numbers)
sum_of_negatives = sum(negative_numbers)
print(positive_numbers)
print(negative_numbers)
print(f'Count of positives: {count_positives}. Sum of negatives: {sum_of_negatives}')