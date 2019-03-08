A = [3,4,5,4,3,5,1,1,2,6,7,2,6]

def solution(A):
    count = {}
    keys = []
    for a in A:
        if a not in keys:
            count[a] = 1
            keys = count.keys()
        else:
            count[a] = 2
            keys = count.keys()
    for i,v in enumerate(count.values()):
        if v == 1:
            index = i
        else:
            continue
    return list(keys)[index]


print(solution(A))


count = {3:1,4:2}