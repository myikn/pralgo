import sys

a = input().split('-')
result = 0

if len(a) == 1:
    for i in a[0].split('+'):
        result += int(i)
    print(result)

else:
    a_sum = 0
    for i in a[0].split('+'):
        a_sum += int(i)
        
    for j in range(1, len(a)):
        tmp = 0
        for k in a[j].split('+'):
            tmp += int(k)
        result += tmp
    print(a_sum - result)