n=int(input("Enter the nUmber:"))
arr=[]
i=0
while(i<n):
    b=int(input())
    arr.append(b)
    i=i+1
arr.sort()
diff=arr[-2]-arr[0]
print("Maximum Difference:",diff)
