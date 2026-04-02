t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    
    arr = list(s)
    arr.sort()
    
    max_char = arr[-1]
    
    ans = ord(max_char) - ord('a') + 1
    
    print(ans)