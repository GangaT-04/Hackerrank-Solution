n=int(input("Enter the Number of Elements:"))
arr=[]
for i in range(0,n):
    arr.append(int(input()))
k=int(input("Enter the number of times rotate an array:"))
m=0
l=0
opos=[]
epos=[]
for i in range(0,n):
    if(i%2==0):
        epos.append(arr[i])
        m=m+1
    else:
        opos.append(arr[i])
        l=l+1
for i in range(0,k):
    temp=opos[l-1]
    j=l-2
    while(j>=0):
        opos[j+1]=opos[j]
        j=j-1
    opos[0]=temp
for i in range(0,k):
    temp=epos[0]
    j=0
    while(j<l):
        epos[j]=epos[j+1]
        j=j+1
    epos[m-1]=temp
k=0
j=0
for i in range(n):
    if(i%2==0):
        print(epos[k])
        k=k+1
   else:
        print(opos[j])
        j=j+1
