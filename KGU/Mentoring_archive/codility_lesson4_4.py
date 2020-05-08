# codility lesson 4.4

A = [1, 3, 6, 4, 1, 2]
# A = [1, 2, 3]
# A = [-1, -2]

# Solution 1
def solution(A):
    i = 1
    for a in sorted(list(set(A))):
        if a <= 0:
            continue
        if a == i:
            i+=1
    print(i)
    return i

solution(A)