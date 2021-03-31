#Input: command = "G()(al)"
#Output: "Goal"
a=str(input())
b=a.replace('(al)','al').replace("()","o") 
print(b)