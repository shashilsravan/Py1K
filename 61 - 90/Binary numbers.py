def generate(number):
    temp = 0
    i = 1
    while i < number:
        if bin(i).replace('0b', '').count('11') == 0:
            temp = bin(i).replace('0b', '')
        i += 1
        print(temp)
    return temp

for _ in range(int(input())):
    num = int(input())
    largest = generate(num)
    print(largest)