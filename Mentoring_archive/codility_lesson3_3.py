A = [3,1,2,4,3]

def solution(A):
    p = 1
    B = []
    while p < len(A):
        a = A[:p]
        # print(a)
        b = A[p:]
        # print(b)
        B.append(abs(sum(a)-sum(b)))
        p += 1
    print(B)
    return min(B)

print(solution(A))