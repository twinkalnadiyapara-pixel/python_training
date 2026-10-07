import json

class READDATA:
    def read_data(self):
        try :
            with open("D:/python-training/src/Employee_Management_System/Data_Json/employee_manager.json","r") as f:
                return json.load(f)
        except Exception as e :
            print(e)

readdata = READDATA()
readdata.read_data()

class SALARYVALIDATION:
    def salary_validation(self):
        employee_data = readdata.read_data()

        for employee in employee_data.values():
            if employee["em_salary"] >= 10000 or employee["em_department"] == "it" :
                print(f"Salary is {employee['em_salary']} , So You will get one day off a month.")
            else :
                print("You won't get a single day off in a month.")

salaryvalidation = SALARYVALIDATION()
salaryvalidation.salary_validation()

class EMPLOYEEELIGIBILITY:
    def employee_eligibility(self):
        employee_data = readdata.read_data()

        for employee in employee_data.values():
            if employee["em_experience"] >= 2 :
                print("Employee Is Eligible")
            else :
                print("Employee Is Not Eligible")

employeeeligibility = EMPLOYEEELIGIBILITY()
employeeeligibility.employee_eligibility()

class EMPLOYEEDISCOUNT:
    def employee_discount(self):
        employee_data = readdata.read_data()

        for employee in employee_data.values():
            if employee["em_salary"] > 1000 :
                discount = employee["em_salary"] * 10 / 100
                print(f"salary + 10 % discount , So Your Salary is {employee['em_salary'] + discount}")
            else :
                print("Your salary is low , So You will not get a discount.")

employeediscount = EMPLOYEEDISCOUNT()
employeediscount.employee_discount()


class EMPLOYEEACCESS:
    def employee_access(self):
        employee_data = readdata.read_data()

        for employee in employee_data.values():
            if employee["em_department"] in "it":
                print("Access Company WIFI Data")
            else :
                print("Can not Access Compsny WIFI Data")

employeeaccess = EMPLOYEEACCESS()
employeeaccess.employee_access()

class SALARYAPPROVAL:
    def salary_approval(self):
        employee_data = readdata.read_data()

        for employee in employee_data.values():
            if employee["em_salary"] > 10000 :
                print("loan approved")
            else :
                print("loan not approved")

salaryapproval = SALARYAPPROVAL()
salaryapproval.salary_approval()


# class RuleEngine:
#     def salary_validation():
#         raise NotImplementedError("Please enter salary....")

# class SALARYVALIDATION:
#     def salary_validation(self):
#         employee_data = readdata.read_data()

#         for employee in employee_data.values():
#             if employee["em_salary"] >= 10000 or employee["em_department"] == "IT" :
#                 print(f"Salary is {employee['em_salary']} , So You will get one day off a month.")
#             else :
#                 print("You won't get a single day off in a month.")

# class EMPLOYEEELIGIBILITY:
#     def salary_validation(self):
#         employee_data = readdata.read_data()

#         for employee in employee_data.values():
#             if employee["em_experience"] >= 2 :
#                 print("Employee Is Eligible")
#             else :
#                 print("Employee Is Not Eligible")

# class EMPLOYEEDISCOUNT:
#     def salary_validation(self):
#         employee_data = readdata.read_data()

#         for employee in employee_data.values():
#             if employee["em_salary"] > 1000 :
#                 discount = employee["em_salary"] * 10 / 100
#                 print(f"salary + 10 % discount , So Your Salary is {employee['em_salary'] + discount}")
#             else :
#                 print("Your salary is low , So You will not get a discount.")

# class EMPLOYEEACCESS:
#     def salary_validation(self):
#         employee_data = readdata.read_data()

#         for employee in employee_data.values():
#             if employee["em_department"] in "IT":
#                 print("Access Company WIFI Data")
#             else :
#                 print("Can not Access Compsny WIFI Data")

# class SALARYAPPROVAL:
#     def salary_validation(self):
#         employee_data = readdata.read_data()

#         for employee in employee_data.values():
#             if employee["em_salary"] > 10000 :
#                 print("loan approved")
#             else :
#                 print("loan not approved")

# ruleengine = [SALARYVALIDATION(), EMPLOYEEELIGIBILITY(), EMPLOYEEDISCOUNT(), EMPLOYEEACCESS(), SALARYAPPROVAL()]
# for ruleengines in ruleengine :
#     print(ruleengines.salary_validation())
