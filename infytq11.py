list_input=list(map(int,input().split(",")))
list_total=[]
length=len(list_input)
for i in range(0,length):
    
    for j in range(i+1,length):
        first=list_input[i]
        second=list_input[j]
        fib_list=[]
        fib_list.append(first)
        fib_list.append(second)
        for k in range(j+1,length):
            if(first+second==list_input[k]):
                fib_list.append(list_input[k])
                first=second
                second=list_input[k]
            if(len(list_total)<len(fib_list)):
                list_total=fib_list
        
if(len(list_total)>2):
    print(list_total)
else:
    print("-1")
