t = int(input())

for _ in range(t):
    n , k = map(int, input().split())
    arr = list(map(int,input().split()))
    
    robin_gold = 0
    count = 0
    
    for ai in arr:
        
        if ai >= k:
            robin_gold += ai
        
        elif ai == 0 and robin_gold  > 0:
            robin_gold -= 1
            count += 1
            
    print(count)