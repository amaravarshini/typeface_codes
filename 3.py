def valid(n):
    while(n!=0):
        r=n%10
        if(r not in l):
            return 0
        n=n//10
    return 1

l=[0,1,2,5,6,8,9]

n=int(input())
c=0
i=0
while(c!=n):
    if(i<10 and i in l):
        c+=1
    elif(i>9):
        if(valid(i)):
            c+=1
    i+=1
print(i)
