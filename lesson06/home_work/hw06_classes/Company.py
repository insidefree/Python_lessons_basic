class Company:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def add_employee(self, employee):
        self.employees.update(employee)

    def get_employees(self):
        return self.employees

    @property
    def get_employee_salary(self):
        to_pay = {}
        for emp in self.employees:
            to_pay.update({self.employees[emp].last_name: self.count_salary(self.employees[emp].salary,
                                                                            self.employees[emp].mandatory_hours,
                                                                            self.employees[emp].worked_hours,
                                                                            self.employees[emp].salary_per_hour)})
        return to_pay

    def count_salary(self, salary, mandatory_hours, worked_hours, salary_per_hour):
        delta_hours = int(mandatory_hours) - int(worked_hours)
        salary = int(salary) - int(delta_hours) * float(salary_per_hour) if int(delta_hours) >= 0 else int(
            salary) + (-2) * int(
            delta_hours) * float(salary_per_hour)
        return salary
