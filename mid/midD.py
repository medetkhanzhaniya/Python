cmd=str(input())
point =str(input())
list_coor=point.split()
x=int(0)
y=int(0)
a=False
for i in range(len(cmd)):
    if cmd[i]=="L":
        x-=1
    elif cmd[i]=="R":
        x+=1
    elif cmd[i]=="U":
        y+=1
    elif cmd[i]=="D":
        y-=1
    if x==int(list_coor[0]) and y==int(list_coor[1]):
        a=True 
        print("Passed")
        break
if a==False:
        print("Missed")