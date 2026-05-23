t = int(input())

for _ in range(t):
    
    s = input()
    
    found = False
    
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            
            found = True
            break
        
    if found:
        print(1)
    else:
        print(len(s))