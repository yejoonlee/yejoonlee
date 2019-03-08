# 코딜리티 레슨 1


def solution(N):
    # write your code in Python 3.6
    list = []
    list2 = []
    for i,num in enumerate(bin(N)[2:]):
        # print(num)
        if num == '1':
            list.append(i)
    # print(list)
    for i in range(len(list)):
        if i == 0:
            continue
        sub = list[i] - list[i-1]
        list2.append(sub)
    if list2 == []:
        return 0
    return max(list2)-1
    pass

a = 333
print(solution(a))
print(bin(a))