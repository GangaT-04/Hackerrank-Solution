n=int(input())
l1=[]
for i in range(n):
    l1.append(int(input()))
k=int(input())
k=k%n
for i in range(1,n-1):
    for j in range(k):
        temp=l1[n-2]
        x=n-2
        while(x>i):
            l1[x]=l1[x-1]
            x=x-1
        l1[x]=temp
for i in range(0,n):
    print(l1[i],end=" ")
        
