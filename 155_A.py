n = int(input())
a = list(map(int, input().split()))

max_so_far = a[0]
min_so_far = a[0]

count = 0

for i in range(1, n):
    if a[i] > max_so_far:
        count += 1
        max_so_far = a[i]
    elif a[i] < min_so_far:
        count += 1
        min_so_far = a[i]
        
print(count)