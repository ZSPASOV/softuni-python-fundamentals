concealed_message = input()
command = input()
while command != 'Reveal':
    args = command.split(':|:')
    if len(args) == 2 and args[0] == 'InsertSpace':
        insert_at = int(args[1])
        concealed_message = concealed_message[:insert_at] + ' ' + concealed_message[insert_at:]
        print(concealed_message)
    if len(args) == 2 and args[0] == 'Reverse':
        if args[1] in concealed_message:
            concealed_message = concealed_message.replace(args[1], '', 1)
            reversed_string = args[1][::-1]
            concealed_message = concealed_message + reversed_string
            print(concealed_message)
        else:
            print('error')
    if len(args) == 3 and args[0] == 'ChangeAll':
        concealed_message = concealed_message.replace(args[1], args[2])
        print(concealed_message)
    command = input()
    if command == 'Reveal':
        print(f'You have a new text message: {concealed_message}')


