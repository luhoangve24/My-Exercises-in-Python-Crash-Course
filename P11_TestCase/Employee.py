# 11.3 Employee
class Employee:
    def __init__(self, first, last, year_salary):
        self.first = first
        self.last = last
        self.year_salary = year_salary

    def give_raise(self, extra = None):
        if extra:
            self.year_salary += extra
        else:
            self.year_salary += 5_000