# +-------------+------------+--------+------------+--------+
# | name        | dob        | f_name | date       | amount |
# +-------------+------------+--------+------------+--------+
# | AnshulKumar | 07/07/1995 | Tamal  | 30/02/2019 |  20000 |
# | RahulKumar  | 07/02/1995 | Manish | 31/03/2019 |  16000 |
# +-------------+------------+--------+------------+--------+
for _ in range(int(input())):
    m, n = map(int, input().split())
    lis = []
    for __ in range(n):
        lis.append([x for x in input().split()])
    u = '+' + '+'.join('-' * (x+2) for x in lis) + '+'
    print(u)