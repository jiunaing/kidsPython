import random
i = 0 
r1cnt= 0
r2cnt = tiecnt=0
while i <10:
    i = i+1
    r1 = random.randint(1,50)
    r2 = random.randint(1,50)
    print("values of r1 and r2:", r1,r2)
    if(r1>r2):
        print("r1 won")
        r1cnt= r1cnt+1
    elif(r1==r2):
        print("it is tie")
        tiecnt= tiecnt+1
    else:
        print("r2 won")
        r2cnt= r2cnt+1
print("r1 won how many times= ",r1cnt)
print("r2 won how many times= ",r2cnt)
print("How many ties= ",tiecnt)
