a, b = map(int,input("Введите координаты первого поля:").split())
c, d = map(int, input("Введите координаты второго поля:").split())
sum1 = a + b
sum2 = c + d
if sum1 % 2 == sum2 % 2:
    print("Yes")
    if sum1 % 2 == 0:
        print("White")
    else:
        print("Black")
else:
    print("No")
