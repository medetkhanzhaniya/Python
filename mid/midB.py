import re 
txt=str(input())
word=str(input())

find =re.search(word,txt)
if find:
    print("First time word occurred in position:",find.start())
else:
    print("Not found")