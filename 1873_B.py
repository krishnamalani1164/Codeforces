t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    a[0] += 1
    
    prod = 1
    
    for x in a:
        prod *= x
        
    print(prod)