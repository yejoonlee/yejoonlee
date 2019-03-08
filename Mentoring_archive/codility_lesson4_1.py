# codility lesson 4.1

# Solution 1
A = [1,2,3,4,6,7]

def solution(A):
    for i in range(len(A)):
        if i+1 not in A:
            print(i+1)
            return 0
    print('good')
    return 1

# Solution 2
def solution2(A):
    for i,a in enumerate(sorted(A)):
        if i+1 != a:
            print(i+1)
            return 0
    print('good')
#     return 1


solution(A)