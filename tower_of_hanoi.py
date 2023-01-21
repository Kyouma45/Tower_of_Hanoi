n=int(input("Enter No.of Disks:"))
def hanoi(n,a,c,b):
    if n==1:
        print("Move disk %d from %s to %s" %(n,a,c))
    else:
        hanoi(n-1,a,b,c)    #moving n-1 disks from a to b using c
        print("Move disk %d from %s to %s" %(n,a,c))    #moving nth disk from a to c
        hanoi(n-1,b,c,a)    #moving n-1 disks from b to c using a

hanoi(n,"A","C","B")