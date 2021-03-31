"""
Задача №3850. Сжатие списка


a = list(input().split())
a = [int(i) for i in a]
for i in range(0,len(a)):
    if a[i]==0:
        del a[i]
        a.append(0)
print(*a) //удаляет только 0 и добавляет в конец листа
"""

a = list(input().split())
a = [int(i) for i in a]
for i in range(len(a)):
    if a[i] != 0:
        print(a[i], end=" ")
for i in range(a.count(0)):
    print(0, end=" ")

