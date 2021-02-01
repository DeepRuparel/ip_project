swaps=int(input())
l1=list(map(int,input().split(",")))
l5=l1
l2=sorted(l1)
l4=l1
l3=[]
for i in range(swaps):
    if(l1==sorted(l2)):
        break
    elif(l1[i]>min(l5[i+1:]) and i+1!=len(l1)):
        temp=0
        ind=l1.index(min(l5[i+1:]))
        l4[ind]=temp
        l4[ind]=l1[i]
        l4[i]=temp
for i in range(swaps):
    l3.append(l2[i])
for i in range(len(l1)-swaps):
    j=swaps+i
    l3.append(l4[j])
print(l3)
