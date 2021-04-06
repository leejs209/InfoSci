# 동전분류기

money = int(input("금액은?(단, 단위는 붙이지 말아주세요)"))

print('500원: ' + str(money // 500) + '개')
print('100원: ' + str((money % 500) // 100) + '개')
print('50원: ' + str((money % 100) // 50) + '개')
print('10원: ' + str((money % 50) // 10) + '개')

# /Users/leejs/PycharmProjects/InfoSci/venv/bin/python /Users/leejs/PycharmProjects/InfoSci/이준성_210406/동전분류기.py
# 금액은?(단, 단위는 붙이지 말아주세요)3330
# 500원: 6개
# 100원: 3개
# 50원: 0개
# 10원: 3개
#
# Process finished with exit code 0
