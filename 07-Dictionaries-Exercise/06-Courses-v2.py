command = input()
all_courses = {}
while command != 'end':
    args = command.split(' : ')
    course = args[0]
    student = args[1]
    if course not in all_courses:
        all_courses[course] = []
    all_courses[course].append(student)
    command = input()



sorted_dict = dict(sorted(all_courses.items(), key = lambda x: -len(x[1])))

for key, value in sorted_dict.items():
    print(f'{key}: {len(sorted_dict[key])}')
    for student_name in sorted(value):
        print(f'-- {student_name}')
