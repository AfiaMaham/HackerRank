from collections import Counter
import math

n = int(input())
arr = list(map(int,input().strip().split()))
total = 0

for i in arr:
    total += i
mean = total / n

arr.sort()
center = n // 2
if n % 2 == 0:
    median = (arr[center - 1] + arr[center]) / 2
else:
    median = arr[center]


count = Counter(arr)
max_freq = max(count.values())
modes = [num for num in count if count[num] == max_freq]
mode = min(modes)

squared_arr = []

for i in range(n):
    squared_arr.append((arr[i]-mean)**2)

total = 0  
for i in range(n):
    total += squared_arr[i]
    
SD = total / n
SD = math.sqrt(SD)

margin = 1.96 * (SD /math.sqrt(n))
lower_bound = mean - margin
upper_bound = mean + margin

print(f"{mean:.1f}")
print(f"{median:.1f}")
print(mode)
print(f"{SD:.1f}")
print(f"{lower_bound:.1f} {upper_bound:.1f}")
        