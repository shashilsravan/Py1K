from math import floor
for _ in range(int(input())):
    print(abs(floor((pow(int(input()), 2))/2 - 1)))
    # (n^2 / 2) - 1