import numpy as np

state_tax_limmit = 613900
tax_free_income_limmit = 22207
tax_rates = {
    "alvesta": 0.3342,
    "växjö": 0.3152,
    "ystad": 0.3129,
    "åmål": 0.3394,
    "statlig": 0.2,
}
# "växjö": 0.3216,


class TaxCalculation:
    def __init__(self, employee):
        self.total_gross = employee.total_gross
        self.county = employee.county
        self.yearly_income = employee.total_year_income
        self.salery_after_tax = employee.total_net
        self.taxebul_income = self.yearly_income - tax_free_income_limmit
        self.state_taxebul_income = self.taxebul_income - state_tax_limmit
        self.state_tax: int = 0
        self.pbb = 52500
        self.reduction_max = 3016

    def get_tax_rate(self):
        for t in tax_rates:
            if self.county in t:
                self.tax_rate = tax_rates[t]

        if self.taxebul_income - self.total_gross >= state_tax_limmit:
            self.tax_rate = self.tax_rate + tax_rates["statlig"]

        elif self.taxebul_income > state_tax_limmit:
            self.state_tax = int(
                self.state_taxebul_income * tax_rates["statlig"])
        else:
            pass

    def calculate_tax(self, employee):
        self.tax = int(self.total_gross * self.tax_rate)
        if self.state_tax > 0:
            self.tax += self.state_tax
        self.salery_after_tax = self.total_gross - self.tax
        employee.total_net = self.salery_after_tax
        self.final_tax_rate = round(self.tax / self.total_gross * 100, 2)
        employee.total_tax = self.tax
        employee.total_year_tax = employee.total_year_tax + self.tax
