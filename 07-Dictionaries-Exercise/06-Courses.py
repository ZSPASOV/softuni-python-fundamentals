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


for key, value in all_courses.items():
    all_courses[key] = sorted(value)

sorted_dict = dict(sorted(all_courses.items(), key = lambda x: -len(x[1])))

for key, value in sorted_dict.items():
    participants = '\n-- '.join(sorted_dict[key])
    print(f'{key}: {len(sorted_dict[key])}\n-- {participants}')
