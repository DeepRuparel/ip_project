n=int(input())
k=int(input())
l1=list(map(int,input().split()))
l2=[0]*int(n+1)
for i in l1:
    l2[i]+=1
for i in range(len(l2)):
    if(l2[i]==k):
        print(i)
        break

