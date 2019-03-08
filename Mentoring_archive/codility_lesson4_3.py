# codility lesson 4.3

A = [3,4,4,6,1,4,4]

# Solution 1
def solution(N, A):
    lN = [0] * N
    for a in A:
        if a <= N:
            lN[a-1] = lN[a-1] + 1
        else:
            lN = [max(lN)] * N
    print(lN)
    return (lN)

solution(5,A)