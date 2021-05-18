e = int(input('1부터 몇까지 소수를 구할까요?'))

print('2',end='')
for a in range(3,e+1):
    result = 0
    for i in range(1,a+1):
        if a %i == 0:
            result += 1
    if result <= 2:
        print(', '+ str(a), end='')