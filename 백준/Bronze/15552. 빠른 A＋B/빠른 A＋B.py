import sys

T = int(sys.stdin.readline())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split()) # 사용자의 엔터까지 입력을 받아버려서 끝에 공백이 발생된 상태로 입력을 받게된다.
    print(a+b)
