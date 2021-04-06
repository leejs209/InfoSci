# 우리나라 유니코드에서 한글 1자는 3바이트이다.
name = 'cho gunhee'

'''
여러 줄로 주석을 걸칠 때에는
#을 사용하지 않고
이와 같이 표시합니다.
'''

print(name[4:7])
print(name[0:10])

# int + float -> float
first = 10.
second = 3
print(type(first), type(second))

plus = first + second
print(type(plus))

# 여러 종류의 연산자
first = int(input('\n첫번째 숫자를 입력하시오'))
second = int(input('두번째 숫자를 입력하시오'))

plus = first + second
minus = first - second
multiply = first * second
divide = first / second
mok = first // second
nam = first % second
jisu = first ** second

print('')
print(first, '+', second, '=', plus)
print(first, '-', second, '=', minus)
print(first, '*', second, '=', multiply)
print(first, '/', second, '=', divide)
print(str(first) + '을', str(second) + '로 나눈 몫은', mok)
print(str(first) + '을', str(second) + '로 나눈 나머지는', nam)
print(str(first) + '^' + str(second), '=', jisu)

# /Users/leejs/PycharmProjects/InfoSci/venv/bin/python /Users/leejs/PycharmProjects/InfoSci/이준성_210406/2_2.py
# gun
# cho gunhee
# <class 'float'> <class 'int'>
# <class 'float'>
#
# 첫번째 숫자를 입력하시오10
# 두번째 숫자를 입력하시오7
#
# 10 + 7 = 17
# 10 - 7 = 3
# 10 * 7 = 70
# 10 / 7 = 1.4285714285714286
# 10을 7로 나눈 몫은 1
# 10을 7로 나눈 나머지는 3
# 10^7 = 10000000
#
# Process finished with exit code 0


x = 100
x = y = z = 50

print(x,y,z)

