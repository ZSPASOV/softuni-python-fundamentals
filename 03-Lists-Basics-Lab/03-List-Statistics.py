n = int(input())
positive_numbers = []
negative_numbers = []
count_positives = 0
sum_of_negatives = 0
for i in range(n):
    number_for_list = int(input())
    if number_for_list >= 0:
        positive_numbers.append(number_for_list)
        count_positives += 1
    else:
        negative_numbers.append(number_for_list)
        sum_of_negatives += number_for_list
print(positive_numbers)
print(negative_numbers)
print(f'Count of positives: {count_positives}. Sum of negatives: {sum_of_negatives}')