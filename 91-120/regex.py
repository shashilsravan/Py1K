import re
string = "ABCABDD"
pattern = r'CAB'
print(re.search(pattern, string).span())
print(re.findall(pattern, string))
# print(re.finditer(pattern, string))