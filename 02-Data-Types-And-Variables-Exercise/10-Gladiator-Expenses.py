lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
gladiator_expenses = 0

for i in range(1, lost_fights_count + 1):
    if i % 2 == 0: # Every second lost game, his helmet is broken.
        gladiator_expenses += helmet_price
    if i % 3 == 0: # Every third lost game, his sword is broken.
        gladiator_expenses += sword_price
    if i % 6 == 0: # When both his sword and helmet are broken in the same lost fight, his shield also brakes.
        gladiator_expenses += shield_price
    #Every second time, when his shield brakes, his armor also needs to be repaired.
    if i % 12 == 0:
        gladiator_expenses += armor_price

print(f'Gladiator expenses: {gladiator_expenses:.2f} aureus')




