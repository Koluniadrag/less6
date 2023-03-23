num = []
a = 1
while a <= 100:
    num.append(a)
    a += 1

res = []
a = 0
while a < len(num):
    if num[a] % 7 == 0 and num[a] % 5 != 0:
        res.append(num[a])
    a += 1
print(res)