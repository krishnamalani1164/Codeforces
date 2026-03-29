n =int(input())

a= list(map(int,input().split()))

l , r = 0 , n - 1

sereja = 0
dima = 0

turn = 0

while l <= r:
    if a[l] > a[r]:
        pick = a[l]
        l += 1
    else:
        pick = a[r]
        r -= 1
        
    if turn == 0:
        sereja += pick
    else:
        dima += pick
        
    turn ^= 1  # switch turn
    
print(sereja,dima)