import re
string=input()
list_char=list(re.findall("[a-zA-z]",string))
list_char.reverse()
for i in range(len(string)):
    if(string[i]=='@' or string[i]=='#'):
        list_char.insert(i,string[i])
print("".join(list_char),end="")        
