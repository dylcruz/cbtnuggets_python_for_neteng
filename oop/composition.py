class Payment:
    def __init__(self, wage, bonus):
        self.wage = wage
        self.bonus = bonus

    def salary(self):
        return (self.wage * 52) + self.bonus
    
class Person:
    def __init__(self, name, height, wage, bonus):
        self.name = name
        self.height = height
        self.obj_payment = Payment(wage, bonus)

    def yearly_wage(self):
        return self.obj_payment.salary()


p1 = Person('Dylan', 73, 2000, 10000)
print(p1.yearly_wage())
print(p1.obj_payment)
