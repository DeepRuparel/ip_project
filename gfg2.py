string=input()
count=0

for i in string:
    if(i=='1'):
        count+=1
m=count*(count-1)
ans=m//2
print(ans)
