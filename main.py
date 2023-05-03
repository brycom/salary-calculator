from employees import person1
from hours_to_pay import HoursToGross
from taxes import TaxCalculation

test_gross = HoursToGross(
    person1.hourly_rate,
    person1.workhours,
    person1.normal_workhours,
    person1.overtime,
    person1.overtime_pay,
    person1.sick_leave_days,
    person1.sickleave_times,
)
test_gross.check_for_overtime()
test_gross.hours_to_gross_salery()
test_gross.gross_sickleav_pay()
test_gross.total_gross_pay()

test_tax = TaxCalculation(
    person1.total_gross, person1.county, person1.total_net)

test_tax.get_tax_rate()
test_tax.calculate_tax()
test_tax.tax_reduction()
print(person1.total_year_income)
