from dataclasses import dataclass


@dataclass
class person:
    employment_number: int
    name: str
    age: int
    county: str
    position: str
    hourly_rate: int

    payout_day: int
    workhours: float
    overtime: float
    sick_leave_days: float
    sickleave_times: int
    vacation_days: int
    manual_permission_required_pay: int
    overtime_pay: float
    total_gross: float
    total_net: float
    total_year_income: float
    normal_workhours: float
    email_addres: str
    employment_number: int
    bank_account: int
    expire_date: str
    account_balence: int
    tax_account_balence: int


person1 = person(
    employment_number=1234,
    name="jenny",
    age=23,
    county="växjö",
    position="chef",
    hourly_rate=142,
    payout_day=25,
    workhours=168,
    overtime=0,
    sick_leave_days=0,
    sickleave_times=0,
    vacation_days=0,
    manual_permission_required_pay=0,
    overtime_pay=1.25,
    total_gross=0,
    total_net=0,
    total_year_income=120000,
    normal_workhours=168,
    email_addres="wollibolli@tramseri.se",
    bank_account=123456789,
    expire_date="2023-04-01",
    account_balence=0,
    tax_account_balence=0
)


@dataclass
class BankAccount:

    bank_account: int
    expire_date: str
    account_balence: int
    tax_account_balence: int


bank_account_1 = BankAccount(
    bank_account=123456789,
    expire_date="2023-04-01",
    account_balence=0,
    tax_account_balence=0)
