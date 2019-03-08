a = [1,2,3,4]
# b = [5]
#
# print(b+a)


def rotation(l,c):
    rotatedList = l
    for i in range(c):
        poped = [rotatedList.pop()]
        rotatedList = poped+rotatedList
    return rotatedList

print(rotation(a,5))


