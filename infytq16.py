import itertools
sum1=int(input())
input_list=list(map(int,input().split(",")))
list_comb=list(itertools.combinations(input_list,4))
print(list_comb)
count=0
for i in list_comb:
    isum=sum(i)
    if(isum==sum1):
        count+=1


print(count)
