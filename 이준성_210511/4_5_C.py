for dan in range(9):
    for k in range(1,10):
        multi = dan*k
        print('{0}*{1}={2}'.format(dan,k,str(multi).rjust(2)),end=' ')
    if dan %3 == 2:
        print()