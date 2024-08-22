
num1 = [2,3,3,1,4,6,1,7]
num2 =  [6,4,3,1,2,1,]

print(set(num1))
print(set(num2))
print(set(num1).union(set(num2)))
print(set(num1) & set(num2))



admin = ('admin123','moder')
name = input('Введи имя пользователя')
password_uname =input('Введите пароль')
password = '1234'
if name in admin and password_uname in password:
    print('Доступ разрешен')
else:
    print("Доступ запрещен")


numbers = [4,3,2,9,12,2]
sum = 0
for i in numbers:
    if i % 2 !=0:
        sum +=i
print(sum * numbers[0])
