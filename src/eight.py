obj_1=10
obj_2=20
if( id(obj_1) == id(obj_2)):
    print("both objects are same")
else:
    print("address are not same")
if( (obj_1) == (obj_2)):
    print("both objects have same identity")
else:
    print("both objects do not have same identity")
    

obj_y=obj_1+1

if( (obj_1 is not obj_2)):
    print("obj_1 and obj_yboth objects have same identity")
else:
    print("both objects  have same identity")
