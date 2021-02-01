def pal(num):
    str1=str(num)
    temp=str1[::-1]
    rev=int(temp)
    x=num+rev
    str2=str(x)
    temp2=str2[::-1]
    rev1=int(temp2)
    if(rev1==x):
        print(rev1)
    else:
        num=x
        pal(num)        

pal(int(input()))
    
   
