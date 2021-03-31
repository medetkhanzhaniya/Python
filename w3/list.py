"""
thislist=["dfg","gfgf","fdg"]
print(len(thislist))

append()   Adds an element at the end of the list
clear()	   Removes all the elements from the list
copy()	   Returns a copy of the list
count()	   Returns the number of elements with the specified value
extend()   Add the elements of a list (or any iterable), to the end of the current list
index()	   Returns the index of the first element with the specified value
insert()   Adds an element at the specified position
pop()	   Removes the element at the specified position
remove()   Removes the item with the specified value
reverse()  Reverses the order of the list
sort()	   Sorts the list


thislist = ["apple", "banana", "cherry"]
print(thislist[1])
    out:banana
    выводит первый элемент 


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
        чекает есть ли элемент в листе 


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) заменяет 1 элемент 
    out:['apple', 'blackcurrant', 'cherry']


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
    out :['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
    out:['apple', 'banana', 'watermelon', 'cherry']


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
    out:['apple', 'banana', 'cherry', 'orange']
    добавляет элемент в конец 


thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
    out:['apple', 'orange', 'banana', 'cherry']


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
    out:['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
    добавляет тропикал в лист


thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
    out:['apple', 'cherry']
    удаляет из листа 


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
    out:['apple', 'cherry']
    удаляет 1 элемент из листа


thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
    out:['apple', 'banana']
    удаляет последний элемент


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
    out:['banana', 'cherry']
    del также удаляет элемент 


thislist = ["apple", "banana", "cherry"]
del thislist
    out: удаляет лист 


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
    out:[]

PRINT ALL ITEMS IN LIST
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

PRINT ALL ITEMS IN LIST
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

PRINT ALL ITEMS IN LIST
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

PRINT ALL ITEMS IN LIST
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
    out:['apple', 'banana', 'mango']
    выводит все слова с буквой а 




newlist = [x for x in fruits if x != "apple"]
//Принимать только те товары, которые не являются "яблоками"




newlist = [x for x in range(10)]
//Вы можете использовать range()функцию для создания итерации



newlist = [x for x in range(10) if x < 5]
//Принимает только числа ниже 5



newlist = [x.upper() for x in fruits]
//Установите значения в новом списке в верхний регистр



newlist = ['hello' for x in fruits]
//Установите все значения в новом списке на 'hello



newlist = [x if x != "banana" else "orange" for x in fruits]



thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
    Сортирует по алфавиту 



thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
    сортирует по возрастанию 



thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
    сортирует по убыванию
    //reverse = True



def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
    //50, 65 , 23, 82, 100
    //сортирует цифры по близости к 50



thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
    //сортирует по лоуер леттер



thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
    //реверс 
    //out:['cherry', 'Kiwi', 'Orange', 'banana']




thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
    //копирует все элементы 
    //['apple', 'banana', 'cherry']




thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
    //копирует все элементы 
    //['apple', 'banana', 'cherry']



list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
    //объединить 2 листа в один 
    //['a', 'b', 'c', 1, 2, 3]



list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)
print(list1)
    //объединить 2 листа в один 
    //['a', 'b', 'c', 1, 2, 3]



list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
    //объединить 2 листа в один 
    //['a', 'b', 'c', 1, 2, 3]"""


