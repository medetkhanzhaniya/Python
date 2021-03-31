cnt=int(input())
arr=str(input())
listt=arr.split()
sett=set()
for i in range(len(listt)):
    sett.add(listt[i])
if(len(sett)==cnt):
    print("YES")
else:
    print("NO")