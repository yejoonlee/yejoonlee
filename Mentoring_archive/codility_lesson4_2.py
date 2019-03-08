# codility lesson 4.2

from yeznable.Mentoring_archive import codility_lesson4_1

A = [1,3,1,4,2,3,5,4]

def solution(X, A):
    if len(list(set(A))) < X:
        print('Type1: frog is never able to jump to the other side of the river')
        return -1

    if codility_lesson4_1.solution(list(set(A))) != 1:
        print('Type2: frog is never able to jump to the other side of the river')
        return -1

    fallen_leaves = []
    for i,a in enumerate(A):
        if a not in fallen_leaves:
            fallen_leaves.append(a)
        if len(fallen_leaves) == X:
            print(i)
            return i


solution(5,A)