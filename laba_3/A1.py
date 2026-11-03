x1, y1, x2, y2 = map(int,input("Введите координаты двух точек х1, у1 и х2, у2: ").split())
print(x1,y1,x2,y2,  sep = ("\n"))
if (x1 > 0 and y1 > 0 and x2 > 0 and y2 > 0):
    print("Yes, I четверть")
elif (x1 < 0 and y1 > 0 and x2 < 0 and y2 > 0):
    print("Yes, II четверть")
elif (x1 < 0 and y1 < 0 and x2 < 0 and y2 < 0):
    print("Yes, III четверть")
elif (x1 > 0 and y1 < 0 and x2 > 0 and y2 < 0):
    print("Yes, IV четверть")
else:
    print("No")
