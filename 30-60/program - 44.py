N = int(input())
array = list(map(int, input().strip().split(" ")))[:N]
tt=sum(array)
l=[]
#print(tt)
for i in range(len(array)):
    if((tt-array[i])%7==0):
        l.append(array[i])
if(len(l)==0):
    print(-1)
else:
    m=min(l)
    print(array.index(m))