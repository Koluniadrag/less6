import random

list1 = []
a = 0
while a < 10:
    list1.append(random.randint(1, 10))
    a += 1

list2 = []
a = 0
while a < 10:
    list2.append(random.randint(1, 10))
    a += 1

list3 = []
a = 0
while a < 10:
    number = list1[a]
    if number in list2 and number not in list3:
        list3.append(number)
    a += 1

print("Первый список чисел:", list1)
print("Второй список чисел:", list2)
print("Общие числа:", list3)