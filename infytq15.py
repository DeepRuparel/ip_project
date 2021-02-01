string=input()
even=[]
odd=[]
count=0
for i in string:
    if(i.isalnum()==False):
        count+=1
    if(i.isdigit()==True):
        if(int(i)%2==0):
            even.append(int(i))
        else:
            odd.append(int(i))
         
                     
if(count%2!=0):
    odd,even=even,odd
e=0
o=0
elen=len(even)
olen=len(odd)
m=max(elen,olen)
for i in range(m):
    if(e!=elen):
        print(even[i],end="")
        e=e+1
        
    if(o!=olen):
        print(odd[i],end="")
        o+=1
        
