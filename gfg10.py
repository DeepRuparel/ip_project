string=input()
stack=[]

for i in string:
    if(i.isdigit()==True):
        stack.append(i)
        continue
    else:
        num2=stack.pop()
        num1=stack.pop()
        ans=0
        if(i=="+"):
            ans=int(num1)+int(num2)
            stack.append(ans)
        elif(i=='-'):
            ans=int(num1)-int(num2)
            stack.append(ans)
        elif(i=="*"):
            ans=int(num1)*int(num2)
            stack.append(ans)
        else:
            ans=int(num1)//int(num2)
            stack.append(ans)
print(stack)
