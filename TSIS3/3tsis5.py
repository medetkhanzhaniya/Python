"""
Задача №3853 Большой сдвиг 

a=list(input().split())
b=input()
#for i in range (len(a)):
a=a[b:]+a[:b]
print(*a)
"""
#lst = [int(i) for i in lst]
#for i in range(len(lst)):

lst = list(input().split())
cal=int(input())
steps=cal%10
if steps>0:
    lst = lst[steps-1:] + lst[:steps-1]
elif steps<0:
    lst=lst[steps+1:]+lst[:steps+1]
print(*lst)