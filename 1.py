def convertToTernary(n):
    s='-' if n<0 else ''
    n=abs(n)
    if(n<3):
        return str(n)
    st=''
    while(n!=0):
        st=str(n%3)+st
        n=n//3
    return s+st

print(convertToTernary(int(input())))
