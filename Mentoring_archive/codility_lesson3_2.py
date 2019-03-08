def solution(X, Y, D):
    jumpCount = 0
    while X < Y:
        X += D
        jumpCount += 1
    return jumpCount

print(solution(10,85,30))