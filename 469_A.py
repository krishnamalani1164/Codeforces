n = int(input())

x = list(map(int,input().split()))
y = list(map(int,input().split()))

set_x = set(x[1:])
set_y = set(y[1:])

total = set_x | set_y

if len(total) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")