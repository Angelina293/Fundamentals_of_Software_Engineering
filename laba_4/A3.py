while True:
    line = input("Ввод:\n")
    
    if len(line) < 5:
        print("Неверный ввод. Длина строки должна быть не меньше 5 символов! Попробуйте снова.")
        print("-" * 30)
        continue
        
    if not all(char in '01' for char in line):
        print("Неверный ввод. Используйте только символы '0' и '1'! Попробуйте снова.")
        print("-" * 30)
        continue
    
    break


total = len(line)  
lost = line.count('0')   

max_seq = 0             
curr_seq = 0

for pkt in line:
    if pkt == '0':
        curr_seq += 1
        if curr_seq > max_seq:
            max_seq = curr_seq
    else:
        curr_seq = 0

pct = (lost / total) * 100  


if pct <= 1:
    status = "отличное качество"
elif pct <= 5:
    status = "хорошее качество"
elif pct <= 10:
    status = "удовлетворительное качество"
elif pct <= 20:
    status = "плохое качество"
else:
    status = "критическое состояние сети"

print("\nВывод:")
print(f"Общее количество пакетов: {total}")
print(f"Количество потерянных пакетов: {lost}")
print(f"Длина самой длинной последовательности потерянных пакетов: {max_seq}")
print(f"Процент потерь:", round(pct, 1), "%")
print(f"Качество связи: {status}")
