import os
from datetime import date

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

pay_period = date.today().strftime("%Y-%m")


def payslip(employee):
    pdf_file_name = f"payslip - {employee.name} - {date.today()}.pdf"
    if os.path.exists(pdf_file_name):
        os.remove(pdf_file_name)

    c = canvas.Canvas(pdf_file_name, pagesize=letter)
    width, height = letter
    # employee info
    c.setFontSize(24)
    c.drawRightString(width / 3, height - inch / 1.5, employee.company)
    c.setFontSize(12)
    c.drawString(inch * 6, height - inch * 0.4,
                 f"Name: {employee.name}")
    c.drawString(inch * 6, height - inch * 0.6,
                 f"Nr: {employee.employment_number}")
    c.drawString(inch * 6, height - inch * 0.8,
                 f"Payout date: {pay_period}-{employee.payout_day}")
    c.drawString(inch * 6, height - inch * 1, f"Pay period: {pay_period}")

    c.setLineWidth(1)
    c.setStrokeColorRGB(0.5, 0.5, 0.5)
    c.line(inch, height - inch * 1.25, width - inch, height - inch * 1.25)
    # setup
    c.setFontSize(12)
    c.drawRightString(inch * 2, height - inch * 2, "Spec:")
    c.drawString(inch * 3, height - inch * 2, "Unit:")
    c.drawString(inch * 4, height - inch * 2, "Rate:")
    c.drawString(inch * 5, height - inch * 2, "Total:")
    # normal work
    c.drawRightString(inch * 2, height - inch * 2.4, "Work hours:")
    c.drawString(inch * 3, height - inch * 2.4,
                 f"{employee.workhours - employee.overtime}h")
    c.drawString(inch * 4, height - inch * 2.4, f"{employee.hourly_rate}kr")
    c.drawString(inch * 5, height - inch * 2.4,
                 f"{employee.total_gross-employee.total_overtime_pay}kr")
    # overtime
    c.drawRightString(inch * 2, height - inch * 2.6, "Overtime:")
    c.drawString(inch * 3, height - inch * 2.6, f"{employee.overtime}h")
    c.drawString(inch * 4, height - inch * 2.6,
                 f"{int(employee.hourly_rate * employee.overtime_pay)}kr")

    c.drawString(inch * 5, height - inch * 2.6,
                 f"{employee.total_overtime_pay}kr")
    # sickleave
    sick_leave_pay = employee.hourly_rate * 8
    c.drawRightString(inch * 2, height - inch * 2.8, "Sick days:")
    c.drawString(inch * 3, height - inch * 2.8,
                 f"{employee.sick_leave_days}days")
    c.drawString(inch * 4, height - inch * 2.8,
                 f"{int(sick_leave_pay * 0.8)}kr")
    c.drawString(inch * 5, height - inch * 2.8,
                 f"{employee.total_sick_pay}kr")

    c.setStrokeColorRGB(0.5, 0.5, 0.5)
    c.line(inch, height - inch * 5, width - inch, height - inch * 5)
    # Monthly
    c.setFontSize(12)
    c.drawRightString(inch * 2, height - inch * 6.2, "Salary:")
    c.drawString(inch * 2.1, height - inch * 6.5,
                 f"Monthly gross pay:   {employee.total_gross}kr")
    c.drawString(inch * 2.1, height - inch * 6.8,
                 f"Monthly tax:   {employee.total_tax}kr")
    c.drawString(inch * 2.1, height - inch * 7.1,
                 f"Monthly nett pay:   {employee.total_net}kr")

    c.setStrokeColorRGB(0.5, 0.5, 0.5)
    c.line(inch, height - inch * 10, width - inch, height - inch * 10)
    # Yearly
    c.setFontSize(12)
    c.drawString(inch * 2, height - inch * 10.5,
                 f"Yearly gross pay:  {employee.total_year_income}kr")
    c.drawString(inch * 5, height - inch * 10.5,
                 f"Yearly tax:{employee.total_year_tax}kr")

    c.save()
