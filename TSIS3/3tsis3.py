"""
a=input().split()
thislist=[]
thislist.extend(a)
#thislist.append(a)
thislist.reverse()
for i in range(len(thislist)):
    thislist[i] = int(thislist[i])
print(thislist)
Задача №3840. Переставить в обратном порядке
"""
a=input().split()
print(*a[::-1])