n=int(input())
nums=[]
for i in range(0,n):
    nums.append(int(input()))
target=int(input())
for i in range(0,n):
    for j in range(i+1,n):
        sum=nums[i]+nums[j]
        if(sum==target):
            print("[{},{}]".format(i,j))
