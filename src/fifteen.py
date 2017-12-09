emp_id=1001
basic_sal=15000.00
allowances=6000.00
mon_gross_sal=basic_sal+allowances
print("emp_id:%d" %emp_id)
print("basic_sal:%d" %basic_sal)
print("allowances:%f" %allowances)
if mon_gross_sal>10000:
    incometax=mon_gross_sal*20/100
    netsalary=mon_gross_sal-incometax
    print("netsalary:Rs.%f" %netsalary)
else:
    netsalary=mon_gross_sal-0.0
  
