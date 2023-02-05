from employees import person1

state_tax_limmit = 613900
tax_rates = {
    "alvesta": 0.3342,
    "växjö": 0.3216,
    "ystad": 0.3129,
    "åmål": 0.3394,
    "statlig": 0.2,
}


class TaxCalculation:
    def __init__(self) -> None:
        self.total_gross = person1.total_gross
        self.county = person1.county
        self.yearly_income = person1.total_year_income

    def get_tax_rate(self):
        for t in tax_rates:
            if self.county in t:
                self.tax_rate = tax_rates[t]

        if self.yearly_income >= state_tax_limmit:
            self.tax_rate += tax_rates["statlig"]
        else:
            pass
        print(f"the tax rate is: {self.tax_rate}%")

    def calculate_tax(self):
        self.tax = int(self.total_gross * self.tax_rate)
        salery_after_tax = self.total_gross - self.tax
        print(f"total tax: {self.tax}kr")
        print(f"salery after taxes:{salery_after_tax}kr")


test_tax = TaxCalculation()


# finde out tax rate for individual by age and county
# check total yearly pay
# calculate taxbasede income
# check taxfree pay
# calculate total tax
