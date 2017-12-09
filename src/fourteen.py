billid=1001
cus_id=101
bill_amount=200.0
dis_bill_amount=0.0
print("billid:%d" %billid)
print("cus_id:%d" %cus_id)
print("bill_amount:%f" %bill_amount)
if (cus_id >100) and (cus_id<=1000) is True:
    if bill_amount>=500:
        dis_bill_amount=bill_amount-bill_amount*10/100
        print("dis_bill_amount=RS.%f" %dis_bill_amount)
    else:
        print("no discount")
else:
    print("invalid customer id,cus_id must be between 101 and 1000")
    
    