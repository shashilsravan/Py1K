def med(arr):
    arr.sort()
    if len(arr) % 2 == 1:
        ret_value = arr[int((len(arr)-1)/2)]
    else:
        ret_value = 0.5*(arr[int(len(arr)/2-1)]+arr[int(len(arr)/2)])
    return ret_value

N = int(input().strip())
x_arr = [int(i) for i in input().strip().split(' ')]
f_arr = [int(i) for i in input().strip().split(' ')]
full_arr = []

for i in range(N):
    for j in range(f_arr[i]):
        full_arr.append(x_arr[i])

Q2 = med(full_arr)

l_arr = [i for i in full_arr if i < Q2]
u_arr = [i for i in full_arr if i > Q2]

Q1 = med(l_arr)
Q3 = med(u_arr)

print('{0:.1f}'.format(Q3 - Q1))