school = 'daeryun'
name = 'hong'
grade = '3'

# %-formatting
print('너의 학교는 %s이고, 이름은 %s이고, 학년은 %s학년이다.' % (school,name,grade))
# str.format()
print('너의 학교는 {0}이고, 이름은 {1}이고, 학년은 {2}학년이다.'.format(school,name,grade))
# f-strings
print(f'너는 학교는 {school}이고, 이름은 {name}이고, 학년은 {grade}학년이다.')
