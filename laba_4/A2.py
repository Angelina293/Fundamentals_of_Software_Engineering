# Запрос размеров у пользователя
n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
ch = '#'
print()
print(f"ПРЯМОУГОЛЬНИК {n}x{m}:")
for i in range(n):              
    for j in range(m):          
        print(ch, end='')       
    print()                     
print()  
print("ПРАВЫЙ ТРЕУГОЛЬНИК:")
for i in range(n):              
    for j in range(i + 1):      
        print(ch, end='')       
    print()                     

print()  

print(f"РАМКА {n}*{m}:")
for i in range(n):              
    for j in range(m):          
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            print(ch, end='')   
        else:
            print(' ', end='')  
    print()                     
