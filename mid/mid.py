import re
pattern="(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@%&?!])[a-zA-z0-9!@%^&*]{8,}"
password=input().split()
username=input()
patter="[a-zA-Z0-9]*#[\d{4}\s]"


if (re.search(pattern,password)) and (re.search(patter,username)):
    print("YES")
else:
    print("NO")
    


