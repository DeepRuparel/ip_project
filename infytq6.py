import re
string=input()

list_num=list(set(re.findall("\d",string)))
list_num.sort(reverse=True)
number=""
number+="".join(list_num)
if(int(number)%2==0):
    print(number)
else:
    length=len(list_num)
    for i in range(length-1,0,-1):
        if(int(list_num[i])%2==0):
            d=list_num[i]
            list_num.remove(d)
            list_num.insert(length-1,d)
            even_num="".join(list_num)
            print(even_num)
            break
    else:
        print("-1")
