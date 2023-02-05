from employees import person1
from hours_to_pay import test_gross
from taxes import test_tax

test_gross.check_for_overtime()
test_gross.hours_to_gross_salery()
test_gross.gross_sickleav_pay()
test_gross.total_gross_pay()
test_tax.get_tax_rate()
test_tax.calculate_tax()
print(f"{person1.total_year_income}kr")
