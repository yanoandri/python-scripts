
def calculate_effective(amount, tenor, interest):
    lists = []
    interest_per_month = interest / 12
    first_balance = amount
    interest_installment = 0.0
    installment = 0
    sum_of_installment = 0
    balance = amount
    lists.append({"interest_installment": interest_installment, "installment": installment, "sum_of_installment": sum_of_installment, "balance" : balance})
    for num in range(0, tenor):
        interest_installment = (balance * interest_per_month) / 100
        installment = (first_balance / tenor)
        sum_of_installment = interest_installment + installment
        balance = balance - installment
        lists.append({ 
            "interest_installment": interest_installment, 
            "installment": installment, 
            "sum_of_installment": sum_of_installment, 
            "balance": balance
        })
    return lists  

def calculate_flat(amount, tenor, interest):
    lists = []
    interest_per_month = interest / 12
    first_balance = amount
    interest_installment = 0.0
    installment = 0
    sum_of_installment = 0
    balance = amount
    lists.append({"interest_installment": interest_installment, "installment": installment, "sum_of_installment": sum_of_installment, "balance" : balance})
    for num in range(0, tenor):
        interest_installment = (first_balance * interest_per_month) / 100
        installment = (first_balance / tenor)
        sum_of_installment = interest_installment + installment
        balance = balance - installment
        lists.append({ 
            "interest_installment": interest_installment, 
            "installment": installment, 
            "sum_of_installment": sum_of_installment, 
            "balance": balance
        })
    return lists  

def format_print(lists):
    for data in lists:
        print(f"Rp. {data['interest_installment']:,f} | Rp. {data['installment']:,f} | Rp. {data['sum_of_installment']:,f} | Rp. {data['balance']:,f}")      
    

loan_amount = int(input('Borrow : '))
loan_tenor = int(input('Tenor : '))
interest_year = float(input('Interest (in %) : '))
calculation_type = input('Effective or flat? ')
if calculation_type == 'effective':
    format_print(calculate_effective(loan_amount, loan_tenor, interest_year))
elif calculation_type == 'flat':
    format_print(calculate_flat(loan_amount, loan_tenor, interest_year))
else:
    print('Unknown calculation')