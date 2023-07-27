from employees import *
from hours_to_pay import HoursToGross
from payslip import payslip
from taxes import TaxCalculation


def main(employee):
    gross = HoursToGross(employee)
    gross.check_for_overtime()
    gross.hours_to_gross_salery()
    gross.gross_sickleav_pay()
    gross.total_gross_pay(employee)

    tax = TaxCalculation(employee)

    tax.get_tax_rate()
    tax.tax_reduction(employee)
    tax.calculate_tax(employee)
    payslip(employee)
    print(f"taxes: {employee.total_tax}")
    print(employee.total_gross * 12)
    print(employee.total_gross)


if __name__ == "__main__":
    main(person2)
