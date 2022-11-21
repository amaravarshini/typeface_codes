a,b=map(str,input().split(','))
l=b[-1]
c=0
for i in a:
    if(i==l):
        c+=1
print(c)
