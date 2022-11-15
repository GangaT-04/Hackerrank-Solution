n=int(input())
r=2*n
start=0
end=r-1
a=[]
k=1
for i in range(0,r):
    b=[]
    for j in range(0,r):
        b.append(0)
    a.append(b)
while(k<=n):
    for i in range(start,end+1):
        for j in range(start,end+1):
            if(i==start or j==start or i==end or j==end):
                a[i][j]=k
    start+=1
    end-=1
    k+=1
    
for i in range(0,r):
    for j in range(0,r):
        print(a[i][j],end=" ")
    print("\r")
