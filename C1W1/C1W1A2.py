#/usr/bin/python3


n = int(input())
numbers = list(int(a) for a in input().split())
maxim1 = numbers[0]
maxim2 = 0
for x in numbers[1:]:
    if x > maxim1:
        maxim1, maxim2 = x, maxim1
    elif x > maxim2:
        maxim2 = x
print(maxim1 * maxim2)
        
