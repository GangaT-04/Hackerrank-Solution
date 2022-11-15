import re
def checkgmail(reg1,gmail):
    if(re.match(reg1,gmail)):
       print("valid mail")
    else:
        print("Invalid mail")

reg1=r'\b[A-Za-z0-9]+@[A-Za-z0-9]+.[A-Za-z]+\b'

gmail=input()
checkgmail(reg1,gmail)
