import random

numb = []
a = 0
while a < 10:
    numb.append(random.randint(0, 10))
    a += 1

max_numb = numb[0]
a = 1
while a < 10:
    if numb[a] > max_numb:
        max_numb = numb[a]
    a += 1

print("Список чисел:", numb)
print("Наибольшее число:", max_numb)