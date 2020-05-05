opens = ["(", "[", "{"]
closes = [")", "]", "}"]
def myFunc(str):
    lis = []
    for s in str:
        if s in opens:
            lis.append(s)
        elif s in closes:
            pos = closes.index(s)
            if ((len(lis) > 0) and
                    (opens[pos] == lis[-1])):
                lis.pop()
            else:
                return False
    return len(lis) == 0


string = input()
print("true" if myFunc(string) else "false")
