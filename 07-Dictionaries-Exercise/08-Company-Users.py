command = input()
company_and_id = {}

while command != 'End':
    args = command.split(' -> ')
    company = args[0]
    id = args[1]
    if company not in company_and_id.keys():
        company_and_id[company] = []
    if id not in company_and_id[company]:
        company_and_id[company].append(id)
    command = input()

company_and_id = dict(sorted(company_and_id.items(), key=lambda x: x[0]))

for key, value in company_and_id.items():
    user_ids = '\n-- '.join(company_and_id[key])
    print(f'{key}\n-- {user_ids}')
