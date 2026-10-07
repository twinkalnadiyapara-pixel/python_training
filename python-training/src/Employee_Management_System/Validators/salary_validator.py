class ISSALARYVALID:

    def __init__(self):
        self.employeesalaryvalid = None

    @property
    def EMPLOYEESALARY(self):
        return self.employeesalaryvalid
      
    @EMPLOYEESALARY.setter
    def EMPLOYEESALARY(self,employeesalary):
        while True :
            employeesalary =int(employeesalary)
    
            if employeesalary <= 0 :
                raise ValueError("salary cannot be negative")

            self.employeesalaryvalid = employeesalary
            break

issalaryvalid = ISSALARYVALID()