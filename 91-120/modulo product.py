import numpy as np
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(np.prod(np.arange(1, a+1)%b, dtype='int64')%b)

# 5
# 506764302 14575
# 10197 17207
# 258166732 90629
# 11420 11789
# 166080323 4784