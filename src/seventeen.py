count=0
while count<=3:
    print(count)
    count+=1
print("loop exceeded")
print("..........................")


#code-2

print("to find sum of first 10 integers ")
result=0
for value in range(1,11):
    result=result+value
print("sum=",result);
print("..........................")


#code-3
num=1
res=0
while num<5:
    res=res+num
    num=num+1
print(res)
print("..........................")

#code-4----for(index=40;index>10;i=i-2)
resu=0
for index in range(40,10,-2):
    if(index%5==0):
        resu=resu+index
        print(resu)
print("..........................")

#code-5
amount=100.0
interest=0.0
months=1
while months<6:
    interest= amount*0.2
    amount=amount+interest
    months+=1
print(amount)
print("..........................")
    
        

