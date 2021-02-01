string=input()
length=len(string)
unique=""
for i in range(length):
    substring=string[i]
    for j in range(i+1,length):
        substring+=string[j]
        sublen=len(substring)
        if(sublen>=3 and len(set(substring))==sublen):
            if(len(unique)<sublen):
                unique=substring
if(len(unique)==0):
    print("-1")
else:
    print(unique)
