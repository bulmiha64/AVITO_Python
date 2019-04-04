def ilen(itetrable):
    return sum(1 for _ in itetrable)

def flatten(aList):
    t = []
    for i in aList:
        if not isinstance(i, list):
             t.append(i)
        else:
             t.extend(flatten(i))
    return t

print(flatten([1,[2,2,3]]))