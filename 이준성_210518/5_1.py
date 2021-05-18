# 약수 구하기
a =  int(input('약수를 구하고 싶은 정수를 입력하세요: '))
for i in range(1,a+1):
    if a %i == 0:
        k = lambda i: '' if i//a else ','
        print(f'{i}',end=k(i))