l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[1,2,3],[4,5,6],[7,8,9]]
result=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(l1)):
    for j in range(len(l2[0])):
        for k in range(len(l2)):
            result[i][j]+=l1[i][k]*l2[k][j]

print("Matrix l1")
for rows in l1:
    for ele in rows:
        print(ele,end=" ")
    print()
        
        
print("Matrix l2")
for rows in l2:
    for ele in rows:
        print(ele,end=" ")
    print()
        
print("result")
for i in range(len(result)):
    for j in range(len(result[0])):
        print(result[i][j],end=" ")
    print()
