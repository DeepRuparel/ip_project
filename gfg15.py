n1,n2=list(map(int,input().split(",")))
string1=input()
string2=input()
commonlen=0
for i in range(n1):
    for x in range(i+1,n1+1):
        s=string1[i:x]
        length=len(s)
        if s in string2:
            if(length>commonlen):
                commonlen=length
print(commonlen)
    
