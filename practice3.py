string=input()
s=""
if(string[0]=="-"):
    s+=string[0]
num=""
for i in string:
    if(i.isdigit()==True):
        num+=i

print(s+num,end="")
    
