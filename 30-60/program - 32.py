# Remove Duplicates from Sorted Array

def removeDuplicates(lis:list):
        i = 1
        while i < len(lis):
            if lis[i] == lis[i-1]:
                lis.remove(lis[i])
            else:
                i += 1
        return lis

lis_ = [int(x) for x in input().split()]
print(removeDuplicates(lis_))