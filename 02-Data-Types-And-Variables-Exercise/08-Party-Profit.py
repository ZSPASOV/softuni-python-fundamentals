party_size = int(input())
days = int(input())
coins = 0

for i in range (1, days + 1):
    if i % 10 == 0: #because in the word file it says beginning of day we put it on top of conditions
        party_size -= 2
    if i % 15 == 0: #because in the word file it says beginning of day we put it on top of conditions
        party_size += 5
    coins += 50
    coins -= 2 * party_size
    if i % 3 == 0:
        coins -= 3 * party_size
    if i % 5 == 0:
        coins += 20 * party_size
        if i % 3 == 0:
            coins -= 2 * party_size


coins_per_person = int(coins / party_size)
print(f'{party_size} companions received {coins_per_person} coins each.')


