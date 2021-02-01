def findMin(occupied_slot):
    m=10
    j=0
    for i in range(0,len(occupied_slot)):
        if(m>occupied_slot[i]):
            m=occupied_slot[i]
            j=i
    return m,j




waiting=int(input("enter the no of slots"))
num=waiting
already_parked=[]
for i in range(1,5):
    already_parked.append(input().split(","))
already_parked.insert(0,"-1")
occupied_slot=[]
for i in range(1,len(already_parked)):
    length=len(already_parked[i])
    occupied_slot.append(length)
slots=['T',"A","B","C","D"]
parked=[]
sum1=sum(occupied_slot)
rem=40-sum1
if(rem>waiting):
    while(waiting!=0):
        waiting=waiting-1
        minimum,position=findMin(occupied_slot)
        while(minimum!=10):
            minimum=minimum+1
            parked.append(slots[position+1]+str(minimum))
            occupied_slot[position]=minimum
    print(parked[0:num])
else:
    print("X")
