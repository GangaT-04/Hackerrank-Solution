n=int(input())
#a=65 UPPERCASE LETTERS
a=97 #lower caseletters
for i in range(n):
    for j in range(i+1):
        print(chr(a),end="  ")
        a=a+1
    print("\r")
    
        
