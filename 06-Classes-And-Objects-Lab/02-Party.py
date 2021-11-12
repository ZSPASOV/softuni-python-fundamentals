class Party:
    def __init__(self):
        self.people = []

this_party = Party()
while True:
    command = input()
    if command == 'End':
        break
    else:
        this_party.people.append(command)

going = ', '.join(this_party.people)
print(f'Going: {going}')
print(f'Total: {len(this_party.people)}')