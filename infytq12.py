string=list("HeLloOWorLDd")
char_list=[]
for i in range(0,len(string)):
    if(string[i]==""):
        continue
    char_grp=string[i]
    for j in range(i+1,len(string)):
        if(string[i].lower()==string[j].lower()):
            char_grp+=string[j]
            string[j]=""
    string[i]=""
    char_list.append(char_grp)
print(char_list)
for i in range(len(char_list)):
    for j in range(i+1,len(char_list)):
        if(char_list[i].lower()>char_list[j].lower()):
            temp=char_list[j]
            char_list[j]=char_list[i]
            char_list[i]=temp
length=len(char_list)
for i in range(len(char_list)//2):
    
    print(char_list[i]+char_list[length-i-1],end="")
if(len(char_list)%2!=0):
    print(char_list[len(char_list)//2])
