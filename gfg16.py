l1=list(input().split(","))
string=l1[0]
deletion=l1[1]
string=string.split(deletion)
ans=0
for i in string:
    ans+=(len(i)*int(len(i)+1)//2)
print(ans)
