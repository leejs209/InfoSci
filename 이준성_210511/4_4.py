for j in range(2):
    for i in range(5):
        if j:
            i = 4-i
        for k in range(4-i):
            print('',end=' ')
        for x in range(2*i+1):
            print('*',end='')
        print()