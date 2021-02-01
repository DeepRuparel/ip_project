input_sting=input()
list1=input_string.split(",")
finalstr=""
for obj in list1:
    temp=obj.split(":")
    name=temp[0]
    number=temp[1]
    length=len(name)
    max1=0
    for digit in number:
        if(int(digit)<=length):
            if(max1<int(digit)):
                max1=int(digit)
   if(max1==0):
       finalstr+="X"
    else:
        finalstr+=name[max1-1]
print(finalstr)
