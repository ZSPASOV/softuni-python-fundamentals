tasks = []

while True:
    command = input()
    if command == 'End':
        break
    tokens = command.split('-', maxsplit=1) # it will split the first occurrance of '-' only
    priority = int(tokens[0])
    task = tokens[1]
    tasks.append((priority, task)) #appending a tuple

tasks_in_priority = [task_name for priority, task_name in sorted(tasks)]
print(tasks_in_priority) # list
#print(tasks) # tuple