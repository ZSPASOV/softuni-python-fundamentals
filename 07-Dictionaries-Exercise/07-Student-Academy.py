n = int(input())
student_grades = {}

for _ in range(n):
    student = input()
    grade = float(input())
    if student not in student_grades.keys():
        student_grades[student] = []
    student_grades[student].append(grade)

student_grades_higher = dict(filter((lambda x: sum(x[1]) / len(x[1]) >= 4.50), student_grades.items()))

sorted_dict = dict(sorted(student_grades_higher.items(), key=lambda x: -(sum(x[1]) / len(x[1]))))
for key, value in sorted_dict.items():
    print(f'{key} -> {sum(value) / len(value):.2f}')