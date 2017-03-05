from lesson06.home_work.hw06_classes.Person import Person


class Employee(Person):
    def __init__(self, id, first_name, last_name, position, salary, mandatory_hours, worked_hours, salary_per_hour):
        Person.__init__(self, id, first_name, last_name)
        self.position = position
        self.salary = salary
        self.mandatory_hours = mandatory_hours
        self.worked_hours = worked_hours
        self.salary_per_hour = salary_per_hour

    def __repr__(self):
        return "{} {} {} {} {}".format(self.first_name, self.last_name, self.position, self.salary,
                                       self.salary_per_hour)
