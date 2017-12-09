bill_id=1001
cus_id=101
bill_amount=200.0
discounted_bill_amount=0.0
print("bill id :%d" %bill_id)
print("customer id:%d" %cus_id )
print("billamount:Rs.%f" %bill_amount)
if bill_amount>500:
    discountedbill_amount=bill_amount-bill_amount *2 / 100
else:
    discountedbill_amount=bill_amount-bill_amount*1 / 100
print("discountedbill_amount:Rs.%f" %discountedbill_amount)