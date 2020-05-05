for _ in range(int(input())):
    n = int(input())
    print("The streak is broken!" if (n % 21 == 0) or ('21' in str(n)) else "The streak lives still in our heart!")
