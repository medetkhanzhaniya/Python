"""

#CREATE A SET:
thisset={"a","b","c"}
print(thisset)



ONCE A SET CREATED 
YOU CANNOT CHANGE ITS ITEMS
BUT YOU CAN ADD NEW ITEMS




#SETS CANNOT HAVE 2 ITEMS WITH SAME VALUE 




thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
    #out:true



    
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
    #add new item to set 
  




thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
    #add elements from one set to another 
    #you can also add elements of a list to at set






#REMOVE ITEMS 
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
    #out:{'apple', 'cherry'}



#REMOVE LAST ITEM 
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
    #cherry
    #{'banana', 'apple'}





#EMPTIES THE SET 
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
    #out:set()
   



#DELETE THE SET COMPLETELY 
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
 




#returns a new set with all items from both sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
    #out:{1, 2, 3, 'a', 'b', 'c'}




#inserts the items in set2 into set1
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)




#union()и update()исключают повторяющиеся элементы.





#ВЫВОДИТ ЭЛЕМЕНТЫ КОТОРЫЕ ЕСТЬ И В СЕТ1 И В СЕТ2
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
    #out:{'apple'}
    





#ДОБАВЛЯЕТ ОБЩИЙ ЭЛЕМЕНТ В НОВЫЙ СЕТ
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z) 
  





#выводит все элементы кроме общих элементы 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x)
    #out:{'microsoft', 'google', 'cherry', 'banana'}




#добавляет все необщие элементы в новый сет 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)
print(z)
    #out:{'google', 'microsoft', 'banana', 'cherry'}






x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)
print(z)
""" 