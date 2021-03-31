#Given an integer number n, return the difference between the product of its digits and the sum of its digits
a=int(input())
sum=0
product=1
while a :
    n=a%10
    product*=n
    sum+=n
    a//=10
print(product-sum)