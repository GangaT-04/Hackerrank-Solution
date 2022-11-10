l1=[2,3,6,8,5,16,65,12]
n=len(l1)
l2=[]
k=0
s=0
for i in l1:
    for j in range(2,i):
        if(i%j==0):
            l2.append(i)
            k+=1
            break
for i in l2:
    s=s+(i*i)
print(s)

            
