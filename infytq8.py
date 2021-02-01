dictionary=input().split(",")
for obj in dictionary:
    temp=obj.split(":")
    string=temp[0]
    number=temp[1]
    length=len(string)
    sum1=0
    for i in number:
        sum1+=int(i)**2
    if(sum1%2==0):
        s=string[length-2:length]
        print(s+string[0:length-2],end=' ')
    else:
        s=string[0]
        print(string[1:length]+s,end=' ')
