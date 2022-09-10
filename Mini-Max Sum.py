def miniMaxSum(arr):
    # Write your code here
    mini=0
    maxi=0
    for i in range(0, len(arr)):    
        for j in range(i+1, len(arr)):    
            if(arr[i] > arr[j]):    
                temp = arr[i];    
                arr[i] = arr[j];    
                arr[j] = temp; 
                   
    for i in range(0,len(arr)-1):
        mini=mini+arr[i]
    for i in range(1,len(arr)):
        maxi=maxi+arr[i]
    print(mini,end=" ")
    print(maxi)
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
