student=[] ##제출한 학생
n_student=[] ##제출하지 않은 학생
for i in range(28): ##제출한 학생들 반복문 돌려서 배열에 입력
    s=int(input())
    student.append(s)
for i in range(1,31):
    if i not in student: ##위 배열에 없는 숫자 제출하지 않은 학생 배열에 입력
        n_student.append(i)
print(min(n_student))
print(max(n_student))