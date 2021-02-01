from itertools import permutations
list_input=list(map(int,input().split(",")))

list_comb=set(permutations(list_input,3))
length=len(list_comb)
maximum=max(list_comb)
m=""
for i in maximum:
    m+=str(i)
print(m,end=",")
print(length,end="")

