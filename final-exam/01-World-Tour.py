holiday_stop = input()
command = input()

while command != 'Travel':
    args = command.split(':')
    action = args[0]
    if action == 'Add Stop':
        index = int(args[1])
        string_to_insert = args[2]
        if index < len(holiday_stop):
            holiday_stop = holiday_stop[:index] + string_to_insert + holiday_stop[index:]
        print(f'{holiday_stop}')
    if action == 'Remove Stop':
        start_index = int(args[1])
        end_index = int(args[2])
        if start_index < len(holiday_stop) and end_index < len(holiday_stop):
            holiday_stop = holiday_stop[:start_index] + holiday_stop[end_index+1:]
        print(f'{holiday_stop}')
    if action == 'Switch':
        old_string = args[1]
        new_string = args[2]
        if old_string in holiday_stop:
            holiday_stop = holiday_stop.replace(old_string, new_string)
        print(holiday_stop)
    command = input()
    if command == 'Travel':
        print(f"Ready for world tour! Planned stops: {holiday_stop}")


