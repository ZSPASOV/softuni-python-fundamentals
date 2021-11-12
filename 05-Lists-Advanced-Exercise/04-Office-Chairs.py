number_rooms = int(input())
chairs_needed = 0
chairs_left = 0
for i in range(number_rooms):
    room = input().split(' ')
    last = int(room.pop())
    chairs_capacity = room[0]
    if last > len(chairs_capacity):
        chairs_needed += last - len(chairs_capacity)
        print(f'{last - len(chairs_capacity)} more chairs needed in room {i + 1}')
    else:
        chairs_left += len(chairs_capacity) - last

if chairs_left >= 0 and chairs_needed == 0:
    print(f'Game On, {chairs_left} free chairs left')
