import random
import time

primer = int(input("Введите количество примеров: "))#количество примеров от пользователя
tima = 0 #счётчик времени 
count = 0 #счётчик текущего вопроса
correct_count = 0 #счётчик правильных ответов

for i in range(primer):
    count += 1
    print(f"Вопрос {count} / {primer}")
    num1, num2 = random.sample(range(2, 10), k = 2)
    num = num1 * num2
    tim_start = time.time()
    while True:
        answer = input(f" {num1} * {num2} = " )
        try:
            answer = int(answer)
            tim_stop = time.time()
            tim = round(tim_stop - tim_start, 1)
            tima = tima + tim

            if answer == num:
                print(f"Верно! (Время: {tim} сек.)")
                correct_count += 1
            else:
                print(f"НЕверно! Правильно: {num} (Время: {tim} сек.)")
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")

if primer > 0:
    average_time = round(tima / primer, 1)
    percent = round((correct_count / primer) * 100, 1)
else:
    average_time = 0
    percent = 0



print("====================================================")
print("СТАТИСТИКА:")
print("====================================================") 
print(f"Общее время: {round(tima, 1)} секунд")
print(f"Среднее время на вопрос: {average_time} секунд")
print(f"Правильных ответов: {correct_count}/{primer}")
print(f"Процент правильных: {percent}%")