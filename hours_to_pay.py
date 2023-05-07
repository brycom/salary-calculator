
class HoursToGross:
    def __init__(
        self, employee
    ):
        self.hourly_rate = employee.hourly_rate
        self.workhours = employee.workhours
        self.normal_workhours = employee.normal_workhours
        self.overtime = employee.overtime
        self.overtime_payrate = employee.overtime_pay
        self.sickleav = employee.sick_leave_days
        self.sickleave_times = employee.sickleave_times
        self.total_gross = []

    def check_for_overtime(
        self,
    ):
        if self.workhours > self.normal_workhours:
            overtime = self.workhours - self.normal_workhours
            self.overtime = self.overtime + overtime
            self.workhours = self.normal_workhours

        else:
            pass

    def hours_to_gross_salery(self):
        gross_normal_workhours = int(self.workhours * self.hourly_rate)
        overtime_payrate = int(self.hourly_rate * self.overtime_payrate)
        self.gross_overtime_workhours = int(self.overtime * overtime_payrate)
        # return gross_normal_workhours, gross_overtime_workhours
        self.total_gross.extend(
            [gross_normal_workhours, self.gross_overtime_workhours])

    def gross_sickleav_pay(self):
        payd_sickleav = self.sickleav - self.sickleave_times
        sickleav_payrate = int(self.hourly_rate * 0.8 * 8)
        self.gross_sickleav = payd_sickleav * sickleav_payrate
        self.total_gross.append(self.gross_sickleav)

    def total_gross_pay(self, employee):
        total_gross = sum(self.total_gross)
        employee.total_gross = total_gross
        employee.total_year_income += total_gross
        employee.overtime = self.overtime
        employee.total_overtime_pay = self.gross_overtime_workhours
        employee.total_sick_pay = int(self.gross_sickleav)
