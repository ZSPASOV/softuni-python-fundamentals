number_people = int(input())
capacity = int(input())
number_courses = 0

if capacity >= number_people:
    print(1)
else:
    if number_people % capacity == 0:
        print(int(number_people / capacity))
    else:
        print(number_people // capacity + 1)