list1=list(input().split("."))
list1.reverse()
for i in range(len(list1)-1):
    print(list1[i],end=".")
print(list1[len(list1)-1])
