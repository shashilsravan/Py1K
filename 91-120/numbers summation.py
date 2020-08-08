mod = pow(10, 9)+7
n = int(input())
sqroot=int(n ** 0.5)
sum_ = (sqroot * (sqroot + 1) * (2 * sqroot + 1)) // 6
ans = 0
for i in range(1, sqroot + 1):
    ans += (i*(i+(n//i))*((n//i)-i+1))
print(ans-sum_)