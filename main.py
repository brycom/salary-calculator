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
    tax.calculate_tax(employee)
    payslip(employee)


if __name__ == "__main__":
    main(person2)
