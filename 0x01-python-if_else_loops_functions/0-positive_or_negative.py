#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{} is positive".format(number))
elif number == 0:
    print("{} is zero".format(number))
else:
    print("{} is negative".format(number))


====================

1-last_digit.py

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
print("Last digit of {} is {} and is ".format(number, digit), end="")
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
