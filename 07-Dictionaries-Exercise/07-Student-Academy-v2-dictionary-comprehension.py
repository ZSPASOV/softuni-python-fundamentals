n = int(input())
student_grades = {}

for _ in range(n):
    student = input()
    grade = float(input())
    if student not in student_grades.keys():
        student_grades[student] = []
    student_grades[student].append(grade)

get_average = lambda x: sum(x) / len(x)

students_average_grades = {key: get_average(value) for (key, value) in student_grades.items() if get_average(value) >= 4.5}

students_average_grades = dict(sorted(students_average_grades.items(), key=lambda x:x[1], reverse=True))

for student, avrg in students_average_grades.items():
    print(f'{student} -> {avrg:.2f}')