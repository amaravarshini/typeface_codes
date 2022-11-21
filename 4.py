matrix = []

for i in range(256):
    row = list(map(int,input().split()))
    matrix.append(row)

top = 256
left = 256

right = 0
bottom = 0

rowl = len(matrix)
coll = len(matrix[0])

for i in range(0,rowl):
    start = 0
    while(start < coll):
        if (matrix[i][start] == 0):
            left = min(left,start)
            break
        start+=1
    
    end = coll - 1
    while(end >=0 ):
        if(matrix[i][end] == 0):
            right = max(end,right)
            break
        end -= 1

    top_start = 0
    while(top_start < rowl):
        if (matrix[top_start][i] == 0):
            top = min(top,top_start)
            break
        top_start+=1

    bottom_end = rowl - 1
    while(bottom_end >= 0):
        if (matrix[bottom_end][i] == 0):
            bottom = max(bottom,bottom_end)
            break
        bottom_end-=1

print((top,left),(top,right),(bottom,left),(bottom,right))
