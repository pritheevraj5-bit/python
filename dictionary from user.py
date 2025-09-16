d={}
n=int(input("number of elements to be added in dictionary"))
for i in range(0,n):
    key=input("enter the key:")
    value=input("enter value:")
    d[key]=value
print("dictionary=",d)
d["age"]=16
print(d)
del d["age"]
print(d)



