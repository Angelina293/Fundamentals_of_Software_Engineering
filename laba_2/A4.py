a, b = map(int, input("Введите 2 числа: ").split())
result = [a, b][a <= b]
print(f"Наибольшее из них: {result}")
