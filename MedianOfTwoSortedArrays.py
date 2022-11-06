n1=int(input("Enter the array1 length:"))
nums1=[]
for i in range(0,n1):
    nums1.append(int(input()))
n2=int(input("Enter the array2 length:"))
nums2=[]
for i in range(0,n2):
    nums2.append(int(input()))
nums3=[]
nums3=nums1+nums2
nums3=sorted(nums3)
l=len(nums3)
mid=(l-1)//2
if(l%2!=0):
    print(nums3[mid])
else:
    print((nums3[mid]+nums3[mid+1])/2.0)
