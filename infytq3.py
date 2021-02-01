def validator(string):
    count=0
    stack=[]
    for i in string:
        if(i=='('or i=='{'or i=='['):
            stack.append(i)
            count=count+1
            continue
        if(len(stack)==0):
            return(count+1)
        r=stack.pop()
        if(r=="(" and i==")"):
            count=count+1
        elif(r=="[" and i=="]"):
            count+=1
        elif(r=="{" and i=="}"):
            count+=1
        else:
            return(count+1)
    if(len(stack)==0):
        return 0
    else:
        return count+1
        
string=input()
print(validator(string))
