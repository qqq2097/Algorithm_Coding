x = int(input())
n = int(input())
sum = 0

for i in range(n): 
    a, b = map(int, input().split())
    k = a*b
    sum += k
    
if sum == x:
    print('Yes')   
else:
     print('No')