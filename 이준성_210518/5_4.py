i = int(input('연도?'))
result = 0

for k in range(0,i+1):
    day_in_year = 365 + int(k%4==0) - int(k%100==0) + int(k%400==0)
    print(k, day_in_year)
    result = result + day_in_year
print(result)