s1=input()
s2=" "
count=1
for i in range(1,len(s1)):
    if(s1[i-1]==s1[i]):
        count+=1
    else:
        s2=s2+s1[i-1]
        s2+=str(count)
        count=1
s2=s2+s1[-1]
s2+=str(count)
print(s2)

        
        
