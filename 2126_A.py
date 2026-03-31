t = int(input())

for _ in range(t):
    x = input()
    
    digits = list(x)
    digits.sort()
    
    print(digits[0])