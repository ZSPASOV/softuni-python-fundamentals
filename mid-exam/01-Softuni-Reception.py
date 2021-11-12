first_efficiency = int(input())
second_efficiency = int(input())
third_efficiency = int(input())
students_count = int(input())
hours_needed = 0

while students_count > 0:
    students_count -= (first_efficiency + second_efficiency + third_efficiency)
    hours_needed += 1
    if hours_needed % 4 == 0:
        hours_needed +=1

print(f'Time needed: {hours_needed}h.')

