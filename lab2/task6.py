a = int(input())
b = int(input())
c = int(input())

if a >= b:
    if a >= c:
        if c >= b:
            print(f'{b} {c} {a}')
        else:
            print(f'{c} {b} {a}')
    else:
        print(f'{b} {a} {c}')

else:
    if b >= c:
        if c >= a:
            print(f'{a} {c} {b}')
        else:
            print(f'{c} {a} {b}')
    else:
        print(f'{a} {b} {c}')