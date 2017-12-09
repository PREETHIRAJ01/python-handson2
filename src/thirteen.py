billid=1001
cus_id=101
bill_amount=1200.0
dis_bill_amount=0.0
discount=0
print("billid:%d" %billid)
print("cus_id:%d" %cus_id)
print("bill_amount:%f" %bill_amount)
if bill_amount>=1000:
    discount=5
elif bill_amount>=500:
    discount=2
else:
    discount=1
dis_bill_amount=bill_amount-bill_amount*discount/100
print("dis_bill_amount=RS.%f" %dis_bill_amount)
    