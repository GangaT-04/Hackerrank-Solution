n=int(input())
k=1
m=1
for i in range(1,n-1):
    for j in range(1,k+1):
        print(m,end=" ")
        m=m+1
    k=k+2
    print("\r")
