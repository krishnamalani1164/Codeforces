t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    max1 = max(a)
    count_max1 = a.count(max1)
    
    if count_max1 > 1:
        max2 = max1
    else:
        max2 = -1
        for x in a:
            if x != max1:
                max2 = max(max2, x)
    
    res = []
    
    for x in a:
        if x == max1:
            res.append(x - max2)
        else:
            res.append(x - max1)
    
    print(*res)