import json 
import logging
from Validators import Integer_Validator , Email_Validator , salary_validator
from Storage import employee_data_json_storage

employeedetail={}

logging.basicConfig(filename="D:/python-training/logs/application.log",
                    level=logging.WARNING, filemode="w", 
                    format="{message}={asctime}:{name}:{levelname}:{process}:{lineno}",
                    datefmt="%d-%b-%y %H:%M:%S",
                    style="{")
        
class ADDEMPLOYEE:
    def add_employee(self):
        print("Add Employee Data")

        while True :
            employeeid : int = Integer_Validator.isinteger.is_integer("Enter employee id : ")  
            
            if employeeid in employeedetail:
                logging.warning("Employee ID already exists.")
                return
            break
                    
        employeename : str = input("Enter employee name : ")

        employeeemail : str | int = Email_Validator.isemailvalid.is_email_valid()
        
        if Email_Validator.isemailexists.is_email_exists(employeeemail):
            logging.warning("Employee email already exists")
            print("Email already exists.")
            return
        
        employeedepartment : str = input("Enter employee Department : ")

        employeesalary = Integer_Validator.issalaryinteger.is_salary_integer("Enter employee salary : ")
        salary_validator.issalaryvalid.EMPLOYEESALARY = employeesalary
            

        employeeexperience : int | float = int(input("Enter employee Experience : "))

        while True :
            employeeperformance : int = int(input("Enter employee Performance : "))

            if 1 <= employeeperformance <= 5 :
                break
            else :
                print("Please Enter Employee Performance between 1 to 5")
                

        employeedetail[employeeid] = {
            "em_id" : employeeid ,
            "em_name" : employeename ,
            "em_email" : employeeemail ,
            "em_department" : employeedepartment ,
            "em_salary" : employeesalary ,
            "em_experience" : employeeexperience ,
            "em_performance" : employeeperformance ,
        }

        employee_data_json_storage.writeemployeedatajson.write_employeedata_json(employeedetail)

        logging.info("Employee Data Successfully Added...")
        print(employeedetail)

addemployeedata = ADDEMPLOYEE()

class UPDATEEMPLOYEE:
    def update_employee(self):
        print("Update Employee Data")

        employeeid = Integer_Validator.isinteger.is_integer("Enter employee id : ")

        if employeeid in employeedetail :
            employeename : int = input("Enter employee name : ")

            employeeemail : str | int = Email_Validator.isemailvalid.is_email_valid()

            if Email_Validator.isemailexists.is_email_exists(employeeemail):
                logging.warning("Employee email already exists")
                print("Email already exists.")
                return

            employeedepartment : str = input("Enter employee Department : ")
        
            employeesalary = Integer_Validator.issalaryinteger.is_salary_integer("Enter employee salary : ")
            salary_validator.issalaryvalid.EMPLOYEESALARY = employeesalary

            employeeexperience : int | float = int(input("Enter employee Experience : "))
            
            while True :
                employeeperformance : int = int(input("Enter employee Performance : "))
            
                if 1 <= employeeperformance <= 5 :
                    break
                else :
                    print("Please Enter Employee Performance between 1 to 5")
                
            employeedetail[employeeid] = {
                "em_name" : employeename ,
                "em_email" : employeeemail ,
                "em_department" : employeedepartment ,
                "em_salary" : employeesalary ,
                "em_experience" : employeeexperience ,
                "em_performance" : employeeperformance ,
            }

            employee_data_json_storage.writeemployeedatajson.write_employeedata_json(employeedetail)

            logging.info("Employee Data Successfully Updated")
            print(employeedetail)

        else :
            logging.warning("ID not found")

updateemployeedata = UPDATEEMPLOYEE()

class DELETEEMPLOYEE:

    def delete_employee(self):

        employeeid : int = Integer_Validator.isinteger.is_integer("Enter employee id : ")

        if employeeid in employeedetail :
            del employeedetail[employeeid]
            logging.info("Employee Data Successfully deleted")
        else :
            logging.warning("Id is not found")

deleteemployeedata = DELETEEMPLOYEE()

class SEARCHEMPLOYEE:
    def search_employee(self):

        employeeid : int = Integer_Validator.isinteger.is_integer("Enter employee id : ")

        with open("D:/python-training/src/Employee_Management_System/Data_Json/employee_manager.json","r") as f :
                employeedetail = json.load(f)

        if str(employeeid) in employeedetail :
            print(employeedetail[str(employeeid)])

        else :
            print("Id is not found")

searchemployeedata = SEARCHEMPLOYEE()

class DISPLAYALLEMPLOYEE:
    def display_all_employees(self):

        with open("D:/python-training/src/Employee_Management_System/Data_Json/employee_manager.json","r") as f :
                employeedetail = json.load(f)

        logging.info("Show All Employee Details")
        print(employeedetail)

displayallemployeedata = DISPLAYALLEMPLOYEE()

class EXITEMPLOYEE:
    @staticmethod
    def exit_employee():
        print("Program Exited Sucessfully...")

exitemployeedata = EXITEMPLOYEE()
