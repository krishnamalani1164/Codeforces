s = input()

count = 0

for ch in s:
    if ch == '4' or ch == '7':
        count += 1
        
count_str = str(count)

if count > 0 and all(c == '4' or c == '7' for c in count_str):
    print("YES")
else:
    print("NO")