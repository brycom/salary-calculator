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

    def tax_reduction(self, employee):
        self.gross_year = self.total_gross * 12

        if self.gross_year < (self.pbb * 0.91):

            print("steg 1")

        elif self.gross_year in range(int(self.pbb * 0.92), int(self.pbb * 3.24)):
            self.a = int((((self.pbb * 0.91) + (self.gross_year *
                                                0.3874) - 36500) * self.tax_rate) / 12)
            print(f"a:{self.a}  b:")
            print("steg 2")

        elif self.gross_year in np.arange(self.pbb * 3.25, self.pbb * 8.08):
            self.reduktion = 1.812 * self.pbb + \
                (0.128 * (self.gross_year - 3.24 * self.pbb) - tax_free_income_limmit)
            if self.reduktion / 12 > self.reduction_max:
                self.reduktion = self.reduction_max

            else:
                self.reduktion = int(self.reduktion / 12)
            print(f"a:{self.reduktion}")
            print("steg 3")

        elif self.gross_year in range(int(self.pbb * 8.09), int(self.pbb * 13.54)):
            self.reduktion = int(
                ((2.432*self.pbb - tax_free_income_limmit)*self.tax_rate)/12)
            print("steg 4")
            print(f"reduktion:{self.reduktion}")

        else:
            self.reduktion = int(
                ((2.432 * self.pbb - 13900)*(self.tax_rate-0.03) - (self.gross_year - (13.54 * self.pbb)))/12)
            if self.reduktion < 0:
                self.reduktion = 0

            print(f"reduktion: {self.reduktion}")
            print("steg 5")
