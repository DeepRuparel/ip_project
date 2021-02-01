string=input()
otp=""
length=len(string)
for i in range(1,length,2):
    otp+=str(int(string[i])**2)
print(otp[0:4])
