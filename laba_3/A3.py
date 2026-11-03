past = int(input("Введите предыдущее значение: "))
present = int(input("Введите текущее значение: "))

if past <= present:
    meaning = present - past
else:
    meaning = (10000 - past) + present

if meaning <= 300:
    s = 21.0
elif meaning <= 600:
    s = 21.0 + (meaning - 300) * 0.06
elif meaning <= 800:
    s = 21.0 + (300 * 0.06) + (meaning - 600) * 0.04
else:
    s = 21.0 + (300 * 0.06) + (200 * 0.04) + (meaning - 800) * 0.025

if meaning > 0:
    price = round(s / meaning, 2)
else:
    price = 0.0
print(f"Предыдущее: {past} Текущее: {present} Использовано: {meaning} К оплате: {s} Ср. цена m^3 {price}")