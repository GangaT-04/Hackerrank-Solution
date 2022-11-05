arr=[3,5,2,8,9,7,4]
n=len(arr)
for i in range(0,n):
    
    for j in range(i+1,n):
        sum=arr[i]+arr[j]
        if(sum==7):
            print(i,j,end=" ")
    print("\r")    
