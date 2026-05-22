t = int(input())

current = 0
maximum = 0

for _ in range(t):
    a , b = map(int,input().split())
    
    current -= a
    current += b
    
    if current > maximum:
        maximum = current
        
print(maximum)