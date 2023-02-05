# normal workhours to pay
# overtime to pay
# sickleav to pay
# manual permission required time to pay
# total pay before taxes minus tax free pay
# taxfree pay
from employees import person1


class HoursToGross:
    def __init__(
        self,
        hourly_rate,
        workhours,
        normal_workhours,
        overtime,
        overtime_payrate,
        sickleav_days,
        sickleave_times,
    ) -> None:
        self.hourly_rate = hourly_rate
        self.workhours = workhours
        self.normal_workhours = normal_workhours
        self.overtime = overtime
        self.overtime_payrate = overtime_payrate
        self.sickleav = sickleav_days
        self.sickleave_times = sickleave_times
        self.total_gross = []

    def check_for_overtime(
        self,
    ):
        if self.workhours > self.normal_workhours:
            overtime = self.workhours - self.normal_workhours
            self.overtime = self.overtime + overtime
            self.workhours = self.normal_workhours
            print(f"ovrtime: {self.overtime}h workhours: {self.workhours}h")

        else:
            pass

    def hours_to_gross_salery(self):
        gross_normal_workhours = int(self.workhours * self.hourly_rate)
        overtime_payrate = self.hourly_rate * self.overtime_payrate
        gross_overtime_workhours = int(self.overtime * overtime_payrate)
        print(
            f"normal pay: {gross_normal_workhours}kr \novertime pay: {gross_overtime_workhours}kr"
        )
        # return gross_normal_workhours, gross_overtime_workhours
        self.total_gross.extend([gross_normal_workhours, gross_overtime_workhours])

    def gross_sickleav_pay(self):
        payd_sickleav = self.sickleav - self.sickleave_times
        sickleav_payrate = int(self.hourly_rate * 0.8 * 8)
        gross_sickleav = payd_sickleav * sickleav_payrate
        # return gross_sickleav
        print(f"sick days:{self.sickleav} \nsick pay: {gross_sickleav}")
        self.total_gross.append(gross_sickleav)

    def total_gross_pay(
        self,
    ):
        total_gross = sum(self.total_gross)
        person1.total_gross = total_gross
        person1.total_year_income += total_gross
        print(f"total: {total_gross}kr")


test_gross = HoursToGross(
    person1.hourly_rate,
    person1.workhours,
    person1.normal_workhours,
    person1.overtime,
    person1.overtime_pay,
    person1.sick_leave_days,
    person1.sickleave_times,
)
