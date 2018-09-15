def problem2(m, n):
    lm, ln = 0, 1
    rm, rn = 1, 0
    cm, cn = lm + rm, ln + rn
    while cm != m and cn != n:
        if m / n < cm / cn:
            print("L", end='')
            rm, rn = cm, cn
        else:
            print("R", end='')
            lm, ln = cm, cn
        cm, cn = lm + rm, ln + rn
    print()


m, n = 0, 0
while m != 1 and n != 1:
    m, n = [int(x) for x in input().split()]
    if m != 1 or n != 1:
        problem2(m, n)
