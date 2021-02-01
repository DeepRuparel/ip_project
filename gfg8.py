n=int(input())
l1=list(map(int,input().split()))
l2=l1.copy()
l2.sort()
dictionary={}
for i in range(n):
    dictionary[l2[i]]=i
for j in range(n):
    print(dictionary[l1[j]],end=" ")
