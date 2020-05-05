import re
count = int(input())
date = 0
other = 0
while count >= 1:
    chat = input()
    l = re.findall('\s*?([0-9]{1,2})\s*', chat)
    l = [int(d) for d in l]
    dte = [d for d in l if (d == 19) or (d == 20)]
    count -= 1
    oth = [d for d in l if ((d >= 1) or (d <= 30)) and (d != 19) and (d != 20)]
    date += len(dte) * 4
    other += len(oth) * 3
    dte = oth = []

print('Date' if date > other else 'No Date')