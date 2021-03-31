"""
One item tuple, remember the commma:
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))





thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
    //tuple() to make a tuple 
    
    
    
    
   
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
    //out:('cherry', 'orange', 'kiwi') 



x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
    //out:('apple', 'kiwi', 'cherry')
    //меняет tuple на list чтобы мменять значения 




YOU CANNOT ADD ITEMS TO A TUPLE 




thistuple =("1", "2")
y=list(thistuple)
y.append("5")
thistuple=tuple(y)
    //меняет tuple на list добавляет элемент и конвертирует в tuple





YOU CANNOT REMOVE ITEMS IN A TUPLE 






thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
    //меняет tuple на list добавляет элемент и конвертирует на tuple






thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)
    //output ERROR  потому что удалили все элементы 
    




fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
    //out : apple
            banana
            ['cherry', 'strawberry', 'raspberry']
    // * используется когда кол-во значении и переменных не совпадают
       остальным переменным присваивается ред
       




fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
    //первый элемент будет грин последний будет рэд остальные тропик потому что *







thistuple=("1","2","3")
for x in range(len(thistuple)):
    print(thistuple[x])
    #print all elements in tuple




thistuple=("1","2","3")
i=0
while i<len(thistuple):
    print(thistuple[i])
    i=i+1
    #print all items with while 



tuple1=("1","2")
tuple2=("a","b","c")
tuple3=tuple1+tuple2
print(tuple3)
    #('1', '2', 'a', 'b', 'c')
    #join two or more tuples 




fruits=("a","b","c")
tuples=fruits*2
print(tuples)
    #out:('a', 'b', 'c', 'a', 'b', 'c')






count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""