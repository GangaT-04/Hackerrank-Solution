n=int(input())
k=0
for i in range(1,n+1):
    k=k+i
    for j in range(k,k-i,-1):
        print(j,end=" ")
    print("\r")
        
