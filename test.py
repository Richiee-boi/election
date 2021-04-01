


def vcounting():
    global vcounting1
    global vcounting2
    global vcounting3
    global vcounting4
    global vcounting5
    global vcounting6
    global vcounting7
    if cb1==1:
        vcounting1 += 1
    
    
    if cb2==1:
        vcounting2+=1


    if cb3==1:
        vcounting3+=1
    

    if cb4==1:
        vcounting4+=1

    
    if cb5==1:
        vcounting5+=1


    if cb6==1:
        vcounting6+=1
    

    if cb7==1:
        vcounting7+=1



vcounting1=0
vcounting2=0
vcounting3=0
vcounting4=0
vcounting5=0
vcounting6=0
vcounting7=0

cb1=1
cb2=1
cb3=1
cb4=1
cb5=0
cb6=1
cb7=0

vcounting()
print(vcounting1,vcounting2,vcounting3,vcounting4,vcounting5,vcounting6,vcounting7)