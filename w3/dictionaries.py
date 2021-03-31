import re
#str=input().split()
str='''
jhgf55ff@56.com
erfgr
rfregr2gr@fg.com
dfgg
'''
pattern=r'[a-z]+[0-9]*[a-z]*@[a-z]+\.com'
match=re.findall(pattern, str)

print(match)