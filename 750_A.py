n , k = map(int,input().split())

total = 0
count = 0

for i in range(1, n + 1):
    
    total += i * 5
    
    if total + k <= 240:
        count += 1
        
    else:
        break
    
print(count)