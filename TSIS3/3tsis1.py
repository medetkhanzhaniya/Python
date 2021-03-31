"""
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
"""
arr=input().split()
for i in range(0,len(arr),2):
    print(arr[i])
