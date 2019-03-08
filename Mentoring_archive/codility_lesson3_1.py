A = [1,2,3,4,5,7,8,9,10]

def solution(A):
    length = len(A)+1
    B = []
    for i in range(length):
        B.append(i+1)
    return sum(B)-sum(A)

print(solution(A))