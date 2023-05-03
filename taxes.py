import numpy as np

from employees import person1

state_tax_limmit = 613900
tax_free_income_limmit = 22207
tax_rates = {
    "alvesta": 0.3342,
    "växjö": 0.3216,
    "ystad": 0.3129,
    "åmål": 0.3394,
    "statlig": 0.2,
}


class TaxCalculation:
    def __init__(self, total_gross, county,  total_net):
        self.total_gross = total_gross
        self.county = county
        self.yearly_income = person1.total_year_income
        self.salery_after_tax = total_net
        self.taxebul_income = self.yearly_income - tax_free_income_limmit
        self.state_taxebul_income = self.taxebul_income - state_tax_limmit
        self.state_tax: int = 0
        self.pbb = 53500

    def get_tax_rate(self):
        for t in tax_rates:
            if self.county in t:
                self.tax_rate = tax_rates[t]

        if self.taxebul_income - self.total_gross >= state_tax_limmit:
            self.tax_rate = self.tax_rate + tax_rates["statlig"]
            print(
                f"taxebul yearly incom:{self.taxebul_income}kr")

        elif self.taxebul_income > state_tax_limmit:
            self.state_tax = int(
                self.state_taxebul_income * tax_rates["statlig"])
            print(f"state tax : {self.state_tax}kr")
            print(f"state taxebul income :{self.state_taxebul_income}kr")
        else:
            print("fattiglapp!!!")

    def calculate_tax(self):
        self.tax = int(self.total_gross * self.tax_rate)
        if self.state_tax > 0:
            self.tax += self.state_tax
        self.salery_after_tax = self.total_gross - self.tax
        person1.total_net = self.salery_after_tax
        self.final_tax_rate = round(self.tax / self.total_gross * 100, 2)
        print(f"state tax {self.state_tax}kr")
        print(f"total tax: {self.tax}kr")
        print(f"salery after taxes:{self.salery_after_tax}kr")
        print(f"the tax rate is: {self.final_tax_rate}%")

    def tax_reduction(self):
        if self.yearly_income < (self.pbb * 0.91):

            print("steg 1")

        elif self.yearly_income in range(int(self.pbb * 0.92), int(self.pbb * 3.24)):
            self.a = (self.pbb * 0.91) + (self.yearly_income *
                                          0.3874) - tax_free_income_limmit
            self.b = self.a / 12
            print(int(self.b))
            print("steg 2")

        elif self.yearly_income in range(int(self.pbb * 3.25), int(self.pbb * 8.08)):
            print("steg 3")

        elif self.yearly_income in range(int(self.pbb * 8.09), int(self.pbb * 13.54)):
            print("steg 4")

        else:
            print("steg 5")

        # finde out tax rate for individual by county!!!
        # check total yearly pay!!!
        # calculate taxbasede income!!!
        # check taxfree pay
        # calculate total tax!!!
