string = input()
count = int(input())
print(string.count('a') * (count // len(string)) + string[:count%len(string)].count('a'))