emp_id=1001
basic_sal=15000.00
allowances=6000.00
mon_gross_sal=basic_sal+allowances
print("emp_id:%d" %emp_id)
print("basic_sal:%d" %basic_sal)
print("allowances:%.2f" %allowances)
print("mon_gross_sal:%.2f" %mon_gross_sal)
if (mon_gross_sal<5000):
    print("nil")
if (mon_gross_sal>=5001) and (mon_gross_sal<=10000):
    incometax=mon_gross_sal*10 / 100
    netsalary=mon_gross_sal-incometax
    print("incometax:%.2f" %incometax)
    print("netsalary:Rs.%f" %netsalary)
if (mon_gross_sal>=10001) and (mon_gross_sal<=20000): 
    incometax=mon_gross_sal*20 / 100
    netsalary=mon_gross_sal-incometax
    print("incometax:%.2f" %incometax)
    print("netsalary:Rs.%f" %netsalary)
if (mon_gross_sal>20000): 
    incometax=mon_gross_sal*30 / 100
    netsalary=mon_gross_sal-incometax
    print("incometax:%.2f" %incometax)
    print("netsalary:Rs.%f" %netsalary)