for _ in range(int(input())):
    number = int(input())
    largest = 2
    while number % 2 == 0:
        number //= 2
    factor = 3
    max_factor = number ** 0.5
    while factor <= max_factor:
        if number % factor == 0:
            largest = factor
            number //= factor
            while not number % factor:
                number //= factor
            if number == 1:
                print(largest)
                break
            max_factor = number ** 0.5
        factor += 2
    else:
        print(number)