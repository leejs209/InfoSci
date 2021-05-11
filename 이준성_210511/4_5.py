for i in range(3):
    print('{0}~{1}단:'.format(i*3+2,i*3+4))
    for k in range(1,10):
        for j in range(2,5):
            dan = i*3+j
            multi = dan*k
            print('{0}*{1}={2}'.format(dan,k,str(multi).rjust(2)),end=' ')
        print('')