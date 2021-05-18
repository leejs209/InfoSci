'''
# 소수 구하기
def yaksu(a: int):
    k = [i for i in range(1,a+1) if a %i == 0]
    return k

a = int(input('a(정수)를 입력하세요'))

if len(yaksu(a)) <= 2:
    print('a는 소수입니다')
else:
    print('a는 소수가 아닙니다.')


# result = [x for x in range(1,10) if len(yaksu(x)) <= 2]
'''
# 리스트 쓰면 안됨;;
a =  int(input('약수를 구하고 싶은 정수를 입력하세요: '))
result = 0
for i in range(1,a+1):
    if a %i == 0:
        result += 1
if result <= 2:
    print('a는 소수입니다')
else:
    print('a는 소수가 아닙니다.')