l1=list(map(int,input().split(" ")))
b=l1[0]
for i in range(len(l1)):
    if(l1[i]==b):
        b=b+1
    else:
        print(b)
        
