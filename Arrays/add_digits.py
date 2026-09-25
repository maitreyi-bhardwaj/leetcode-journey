def addDigits(num):
    if num == 0:
        return 0

    return 1 + (num - 1) % 9


# Test cases
print(addDigits(38))   # 2
print(addDigits(0))    # 0
print(addDigits(27))   # 9
print(addDigits(999))  # 9


def addDigits(num):
    while num >= 10:
        total = 0

        while num > 0:
            total += num % 10
            num //= 10

        num = total

    return num


# Test cases
print(addDigits(38))   # 2
print(addDigits(0))    # 0
print(addDigits(27))   # 9