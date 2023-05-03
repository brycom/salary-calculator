# sett payout to the payout date
# reserv payout to to the account
# comfirm payout
# send confirmation to employer
# send specification to employee
from datetime import date, datetime

from employees import person1, BankAccount


class Payout:
    def __init__(self, card_number, expiry_date, employe) -> None:
        self.card_number = card_number
        self.expiry_date = date.fromisoformat(expiry_date)
        self.employe = employe

    # def get_card_info(self):

    def check_card(self):
        try:
            if self.expiry_date < date.today():
                raise ValueError("your card is expired")
            if len(str(self.card_number)) != 9:
                raise ValueError("invalid card")

        except ValueError as err:
            print(err)

        else:
            print("your card works!")

    def payout(self):


test = Payout(person1.bank_account, person1.expire_date, person1)

test.check_card()
