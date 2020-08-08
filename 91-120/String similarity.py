def func():
    sim = [0] * len(W)
    sim[0] = len(W)
    pos = 1
    l = 0
    while True:
        if pos + l < len(W) and W[pos + l] == W[l]:
            l += 1
        else:
            if pos >= len(W):
                break
            if l == 0:
                pos += 1
                continue
            sim[pos] = l
            flag = l
            i = 1
            while i < l:
                if W[pos + i] == W[0]:
                    if sim[i] != l - i:
                        sim[pos + i] = min(l - i, sim[i])
                    else:
                        flag = i
                        break
                i += 1
            pos += flag
            l -= flag
    print(sum(sim))

for i in range(int(input())):
    W = input()
    func()
