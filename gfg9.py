n=int(input())
l1=list(map(int,input().split()))
l2=[0]*int(n+1)
for i in l1:
    l2[i]+=1
m=max(l2)
j=l2.index(m)
if(m>n/2):
    print(j)
else:
    print(-1)
