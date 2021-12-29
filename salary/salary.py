class Salary:

    def __init__(self, name, gross_salary, tax):
        self.__name = name
        self.__gross_salary = gross_salary
        self.__tax = tax

    def salary(self):
        sala = self.__gross_salary - self.__tax
        return f"Employee: {self.__name}, $ {sala:.2f}"

    def increase(self, percentage):

        incr =  (self.__gross_salary * percentage / 100) + (self.__gross_salary - self.__tax)
        return f"Update: {self.__name}, $ {incr:.2f}"

