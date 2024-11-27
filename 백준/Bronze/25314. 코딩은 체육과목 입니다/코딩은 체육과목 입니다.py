n = int(input())
answer = 'long int'
if n==4:
    print('long int')
else:
    a = n-4   
    b = a//4

    for i in range(b):
        answer =  'long ' + answer
    print(answer)