#minimum array sum
n=int(input())
lst=list(map(int,input().split()))
lst.sort()
a,b=lst[-1],lst[-2]
avg=(a+b)/2
for i in range(n):
    if lst[i]:
        