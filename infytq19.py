def returnmin(alread_parked):
    m=10
    j=0
    for i in range(0,len(occupied_slot)):
        if(m>occupied_slot[i]):
            m=occupied_slot[i]
            j=i   
    return m,j

waiting=int(input("Enter the no of cars to be parked"))
already_parked=[]
num=waiting
for i in range(1,5):
    already_parked.append(input().split(","))
already_parked.insert(0,"-1")

occupied_slot=[]
for i in range(1,len(already_parked)):
            length=len(already_parked[i])
            occupied_slot.append(length)
print(occupied_slot)
slots=['T','A','B','C','D']
added=[]
sum1=sum(occupied_slot)
rem=40-sum1
if(rem>waiting):
    while(waiting!=0):
        waiting=waiting-1
        minimum,position=returnmin(already_parked)
        
        while(minimum!=10):
            minimum=minimum+1
            added.append(slots[position+1]+str(minimum))
            occupied_slot[position]=minimum
               
        


    print(added[0:num])
else:
    print("X")
    


    
