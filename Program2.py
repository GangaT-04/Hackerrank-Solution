l1=[1,2,3]
l2=[]
start=l1[0]
end=l1[-1]
k=0
for i in range(start,end):
        l2.append(start)
        start=start+1
        k=k+1
for i in l2:
    if i not in l1:
        print(i,end=" ")
        
