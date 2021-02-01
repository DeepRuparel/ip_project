str1=input()
str2=input()
count=0
len1=len(str1)

len2=len(str2)
if(len1>len2):
    for i in str1:
        if i in str2:
            count=count+2
else:
    for i in str2:
        if i in str1:
            count=count+2
total=len1+len2-count
print(total)
