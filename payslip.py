import os
from datetime import date

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas

import employees

# Set up company name and pay information
company_name = "Mathias Brynof"
employee_name = "Mathias Brynolf"
employee_number = "12345"
payout_day = 25
pay_period = date.today().strftime("%Y-%m")
payout_date = f"{pay_period}-{payout_day}"
work_hours = 160
hourly_rate = 20
overtime_hours = 10
overtime_rate = 30
sick_days = 3
sick_day_rate = 100
monthly_gross_pay = int((work_hours * hourly_rate) +
                        (overtime_hours * overtime_rate) + (sick_days * sick_day_rate))
monthly_tax = int(monthly_gross_pay * 0.3)
yearly_gross_pay = int(monthly_gross_pay * 12)
yearly_tax = int(yearly_gross_pay * 0.3)


class PaySlip:
    def __init__(self, employee):
        self.company_name = "Mathias Brynof"
        self.employee_name = employee.name
        self.employee_number = employee.employment_number
        self.payout_day = employee.payout_day
        self.pay_period = date.today().strftime("%Y-%m")
        self.payout_date = f"{pay_period}-{employee.payout_day}"
        self.work_hours = employee.workhours
        self.hourly_rate = employee.hourly_rate
        self.overtime_hours = employee.overtime
        self.overtime_rate = employee.overtime_pay
        self.sick_days = employee.sick_leave_days
        self.sick_day_rate = 100


pdf_file_name = f"payslip - {employee_name} - {date.today()}.pdf"
if os.path.exists(pdf_file_name):
    os.remove(pdf_file_name)


c = canvas.Canvas(pdf_file_name, pagesize=letter)
width, height = letter

c.setFontSize(24)
c.drawRightString(width / 3, height - inch / 1.5, company_name)
c.setFontSize(12)
c.drawString(inch * 6, height - inch * 0.4,
             f"name:{employee_name}")
c.drawString(inch * 6, height - inch * 0.6, f"nr:{employee_number}")
c.drawString(inch * 6, height - inch * 0.8, f"payout date:{payout_date}")
c.drawString(inch * 6, height - inch * 1, f"pay period:{pay_period}")

c.setLineWidth(1)
c.setStrokeColorRGB(0.5, 0.5, 0.5)
c.line(inch, height - inch * 1.25, width - inch, height - inch * 1.25)

c.setFontSize(12)
c.drawRightString(inch * 2, height - inch * 2, "Spec:")
c.drawString(inch * 3, height - inch * 2, "unit")
c.drawString(inch * 4, height - inch * 2, "rate")
c.drawString(inch * 5, height - inch * 2, "total")
# normal work
c.drawRightString(inch * 2, height - inch * 2.4, "Work hours:")
c.drawString(inch * 3, height - inch * 2.4, f"{work_hours}h")
c.drawString(inch * 4, height - inch * 2.4, f"{hourly_rate}kr")
c.drawString(inch * 5, height - inch * 2.4, f"{monthly_gross_pay}kr")
# overtime
c.drawRightString(inch * 2, height - inch * 2.6, "overtime:")
c.drawString(inch * 3, height - inch * 2.6, f"{overtime_hours}h")
c.drawString(inch * 4, height - inch * 2.6, f"{overtime_rate}kr")
c.drawString(inch * 5, height - inch * 2.6,
             f"{overtime_hours * overtime_rate}kr")
# sickleave
c.drawRightString(inch * 2, height - inch * 2.8, "sick days:")
c.drawString(inch * 3, height - inch * 2.8, f"{sick_days}days")
c.drawString(inch * 4, height - inch * 2.8, f"{sick_day_rate}kr")
c.drawString(inch * 5, height - inch * 2.8,
             f"{sick_days * sick_day_rate}kr")


c.setStrokeColorRGB(0.5, 0.5, 0.5)
c.line(inch, height - inch * 5, width - inch, height - inch * 5)
# Monthly
c.setFontSize(12)
c.drawRightString(inch * 2, height - inch * 6.2, "Salary:")
c.drawString(inch * 2.1, height - inch * 6.5,
             f"Monthly gross pay:   {monthly_gross_pay}kr")
c.drawString(inch * 2.1, height - inch * 6.8,
             f"Monthly tax:   {monthly_tax}kr")

c.setStrokeColorRGB(0.5, 0.5, 0.5)
c.line(inch, height - inch * 10, width - inch, height - inch * 10)
# Yearly
c.setFontSize(12)
c.drawString(inch * 2, height - inch * 10.5,
             f"Yearly gross pay:  {yearly_gross_pay}kr")
c.drawString(inch * 5, height - inch * 10.5, f"Yearly tax:{yearly_tax}kr")


c.save()


# test = PaySlip(employees.person1)
# test.test()
