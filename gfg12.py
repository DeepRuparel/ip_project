def calculator(string):
    length=len(string)
    l1=list(string)
    for i in range(length):
        if(l1[i]=="#"):
            for j in range(i-1,-1,-1):
                if(l1[j].isalpha()==True):
                    if(l1[j]=="Z"):
                        l1[j]="A"
                        break
                    else:
                        l1[j]=chr(ord(l1[j])+1)
                        break

    return("".join(l1))


s1=input()
s2=input()
st1=calculator(s1)
st2=calculator(s2)
string1="".join(st1.split("#"))
string2="".join(st2.split("#"))

print(string1)
print(string2)
if(string1==string2):
    print("Yes")
else:
    print("no")
