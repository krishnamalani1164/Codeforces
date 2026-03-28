t = int(input())

for _ in range(t):
    a = list(map(int,input().split()))
    
    for _ in range(5):
        a.sort()
        a[0] += 1
        
    print(a[0] * a[1] * a[2])