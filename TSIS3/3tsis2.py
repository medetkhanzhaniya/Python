#Наименьший положительный
ans=1000
for i in list(map(int, input().split())):
    if 0<i<ans:
        ans=i
print(ans)

