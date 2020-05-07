string = input()
result = ""
for i in range(1, len(string) + 1):
    result += string[:i]
print(result)