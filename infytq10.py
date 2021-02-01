rem=int(input())
list_num=list(map(int,input().split(" ")))
digit=[]
l1=set(list_num)
length=len(l1)
for i in l1:
    count=list_num.count(i)
    digit.append(count)

digit.sort()

length=len(digit)
for count in digit:
    if(int(count)<=rem):
        rem=rem-count
        length=length-1
    else:
        break
print(length)
