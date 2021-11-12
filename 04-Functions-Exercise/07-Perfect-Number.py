def identify_perfect(number):
    perfect_check = "It's not so perfect."
    positive_divisors = []
    if number % 2 == 0:
        for i in range(1, int((number +2) / 2)):
            if number % i == 0:
                positive_divisors.append(i)
        if sum(positive_divisors) == number:
            perfect_check = "We have a perfect number!"
    else:
        for i in range(1, int((number +1) / 2)):
            if number % i == 0:
                positive_divisors.append(i)
        if sum(positive_divisors) == number:
            perfect_check = "We have a perfect number!"

    return perfect_check

check_num = int(input())
print(identify_perfect(check_num))

#note - in range we stop the cycle at half the number, because after that it cannot be a perfect divisor.