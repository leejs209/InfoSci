# int(수,진수)
"""
num_sys = input('원하는 진수를 입력하세요(2/8/10/16):')
val = int(input('변환을 원하는 수를 입력하세요:'),int(num_sys))
print('2진수: {}'.format(bin(val)))
print('8진수: {}'.format(oct(val)))
print('10진수: {}'.format(val))
print('16진수: {}'.format(hex(val)))
"""

# 조건문을 이용
num_sys = int(input('원하는 진수를 입력하세요(2/8/10/16):'))
k = input('변환을 원하는 수를 입력하세요:')
if num_sys == 2:
    val = int(k,2)
elif num_sys == 8:
    val = int(k, 8)
elif num_sys == 10:
    val = int(k, 10)
elif num_sys == 16:
    val = int(k, 16)

print('2진수: {}'.format(bin(val)))
print('8진수: {}'.format(oct(val)))
print('10진수: {}'.format(val))
print('16진수: {}'.format(hex(val)))

# 직접 만든 버전
"""
num_sys = input('원하는 진수를 입력하세요(1~16):')
val = input('변환을 원하는 수를 입력하세요:')

result = 0

chars = ['A','B','C','D','E','F']

def to_dec(x):
    if x in chars:
        for k in range(len(chars)):
            if x == chars[k]:
                return k + 10
    else:
        return int(x)

for k in range(len(val)):
    result += to_dec(val[len(val) - k - 1]) * (int(num_sys)**k)

print('2진수: {}'.format(bin(result)))
print('8진수: {}'.format(oct(result)))
print('10진수: {}'.format(result))
print('16진수: {}'.format(hex(result)))
"""
