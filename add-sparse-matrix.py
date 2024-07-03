matrix1=[[0,0,0,1,0],[2,0,0,0,3],[0,0,0,4,0]]
matrix2=[[0,1,0,4,0],[0,0,0,3,0],[1,4,0,0,2]]

def convert(matrix):
    dct={}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]!=0:
                dct[i,j]=matrix[i][j]
    return dct
    
dicmat1=convert(matrix1)
dicmat2=convert(matrix2)

def add_sparse(first,second):
    result_dict={}
    all_keys=list(first.keys())+list(second.keys())
    for key_iterator in all_keys:
        first_value=first.get(key_iterator,0)
        second_value=second.get(key_iterator,0)
        sum=first_value+second_value
        if sum!=0:
            result_dict[key_iterator]=sum
    return result_dict
    
res=add_sparse(dicmat1,dicmat2)
print(res)
