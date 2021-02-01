import itertools
string=list(input().split(" "))
l2=list(itertools.permutations(string,4))
max=0
for i in l2:
    s1="".join(i)
    n=int(s1)
    if(max<n):
        max=n
    
print(max)   

