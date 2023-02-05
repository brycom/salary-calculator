from dataclasses import dataclass


@dataclass
class person:
    employment_number: int
    name: str
    age: int
    county: str
    position: str
    hourly_rate: int
    payout_account: int
    payout_day: int
    workhours: float
    overtime: float
    sick_leave_days: float
    sickleave_times: int
    vacation_days: int
    manual_permission_required_pay: int
    overtime_pay: float
    total_gross: float
    total_year_income: float
    normal_workhours: float
    email_addres: str


person1 = person(
    employment_number=1234,
    name="johan",
    age=12,
    county="alvesta",
    position="simp",
    hourly_rate=210,
    payout_account=13456789,
    payout_day=25,
    workhours=52,
    overtime=0,
    sick_leave_days=5,
    sickleave_times=2,
    vacation_days=0,
    manual_permission_required_pay=0,
    overtime_pay=1.25,
    total_gross=0,
    total_year_income=600000,
    normal_workhours=40,
    email_addres="wollibolli@tramseri.se",
)
# name
# age
# county
# position
# employment number
# payout account
# payout day
# workhours
# overtime
# sick leave
# vacation days
# manual permission required pay
# normal workhours
# overtime pay
# total pay for year
