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
        self.reduktion = 0

    def get_tax_rate(self):
        for t in tax_rates:
            if self.county in t:
                self.tax_rate = tax_rates[t]

        if self.taxebul_income - self.total_gross >= state_tax_limmit:
            self.tax_rate = self.tax_rate + tax_rates["statlig"]

        elif self.taxebul_income > state_tax_limmit:
            self.state_tax = int(self.state_taxebul_income * tax_rates["statlig"])
        else:
            pass

    def calculate_tax(self, employee):
        self.tax = int(self.total_gross * self.tax_rate)
        if self.state_tax > 0:
            self.tax += self.state_tax
        self.salery_after_tax = (self.total_gross - self.tax) + self.reduktion
        employee.total_net = self.salery_after_tax
        self.final_tax_rate = round(self.tax / self.total_gross * 100, 2)
        employee.total_tax = self.tax - self.reduktion
        employee.total_year_tax = employee.total_year_tax + employee.total_tax
        print(self.tax)

    def tax_reduction(self, employee):
        self.gross_year = self.total_gross * 12

        if self.gross_year < 43953:
            print("steg 1")

        elif self.gross_year in range(43954, 156492):
            self.reduktion = int(
                (
                    (0.3874 * (self.gross_year - 43953) - tax_free_income_limmit)
                    * self.tax_rate
                )
                / 12
            )
            print(f"reduktion:{self.reduktion}")
            print("steg 2")

        elif self.gross_year in range(156493, 390264):
            self.reduktion = int(
                (
                    (
                        0.128 * (self.gross_year - 156492 + 87519.6)
                        - tax_free_income_limmit
                    )
                    * self.tax_rate
                )
                / 12
            )

            self.reduktion = int(self.reduktion / 12)
            print(f"reduktion:{self.reduktion}")
            print("steg 3")

        elif self.gross_year in range(390265, 653982):
            self.reduktion = int(
                ((117465.6 - tax_free_income_limmit) * self.tax_rate) / 12
            )
            print("steg 4")
            print(f"reduktion:{self.reduktion}")

        else:
            self.the_cut = 0.03 * (self.gross_year - 653982)
            self.reduktion = int(
                ((self.tax_rate * (117465.6 - tax_free_income_limmit)) - self.the_cut)
                / 12
            )
            if self.reduktion < 0:
                self.reduktion = 0

            print(f"reduktion: {self.reduktion}")
            print("steg 5")

        return self.reduktion
