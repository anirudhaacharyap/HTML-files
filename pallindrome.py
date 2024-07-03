def check_pallin(string):
    rev=""
    for i in string:
        rev=i+rev
    print("Reversed string=",rev)
    if string==rev:
        return True
    else:
        return False
        
str=input("ENter string:")
print(check_pallin(str))
