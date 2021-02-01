num_list=input().split(",")
length=len(num_list)
num1=0
num2=''
index_five=num_list.index("5")
index_eight=num_list.index("8")
for i in range(index_five,index_eight+1):
    num2+=num_list[i]
for i in range(0,length):
    if(i<index_five or i>index_eight):
        num1=num1+int(num_list[i])
print(num1+int(num2))
