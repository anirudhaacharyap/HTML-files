l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[1,2,3],[4,5,6],[7,8,9]]
result=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(l1)):
    for j in range(len(l1[0])):
        result[i][j]=l1[i][j]+l2[i][j]

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
for rows in result:
    for ele in rows:
        print(ele,end=" ")
    print()
