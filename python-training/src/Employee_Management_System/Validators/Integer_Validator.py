import logging


class ISINTEGER:
    def is_integer(self,prompt):
        while True :
                try :
                    employeeid = int(input(prompt))
                    if employeeid == " ":
                        print("Please Enter id")
                        continue
                    return employeeid
                
                except ValueError:
                    logging.error("ID entered is not an integer")
                    print("Please enter valid number")
isinteger = ISINTEGER()

class ISSALARYINTEGER:
    def is_salary_integer(self ,prompt):
        while True :
            try :
                employeesalary = int(input(prompt))
                                
                if employeesalary <= 0:
                    print("Please salary enter graterthan 0")
                    continue
                return employeesalary
            except :
                logging.error("Salary entered is not an integer")
issalaryinteger = ISSALARYINTEGER()
