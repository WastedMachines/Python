# ===== Ejercicio 12 =====

"""
Exercise 12: Calculate income tax
Calculate income tax for the given income by adhering to the rules below

Taxable Income	    Rate (in %)
First $10,000	    0
Next $10,000	    10
The remaining	    20

For example, suppose the income is 45000, and the income tax payable is

10000*0% + 10000*10%  + 25000*20% = $6000
"""

income = int(input("Digite el ingreso: "))
tax_payable = 0

if income <= 10000:
    print("El ingreso es:", income, "\n Usted no paga impuestos")
    tax_payable = 0

elif income <= 20000:
    x = income - 10000
    tax_payable = x *0.1
else:
    tax_payable = 0

    tax_payable = 10000 * 0.1

    tax_payable += (income - 20000) * 0.2

print("El impuesto total a pagar es de:", tax_payable)
