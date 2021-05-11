#%% while문 이용해 구구단 출력하기
dan = 2
while dan < 10:
    i = 1
    print(f"{dan}단 시작")
    while i < 10:
        multi = dan * i
        print("{0} * {1} = {2}".format(dan,i,str(multi).rjust(2)))
        i += 1
    dan += 1