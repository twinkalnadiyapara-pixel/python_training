import json

class LOADDATA:
    @staticmethod
    def load_data():
        with open("D:/python-training/src/Employee_Management_System/Data_Json/employee_manager.json","r") as f :
            return json.load(f)
loaddata = LOADDATA
loaddata.load_data()

class MINMAXAVG:
    def min_max_avg(self):
        employeedetail = loaddata.load_data()

        salaries = []

        for employee in employeedetail.values():
                salary = employee["em_salary"]
                salaries.append(salary)
        
        averge = sum(salaries) / len(salaries)

        print("Employee Lowest Salary : ", min(salaries))
        print("Employee Highest Salary : ", max(salaries))
        print("Employee Average salary : ",averge )
minmaxavg = MINMAXAVG()
minmaxavg.min_max_avg()

class SORTING:
    def sorting(self):
        employeedetail = loaddata.load_data()

        experiences = []
        names = []

        for employee in employeedetail.values():
            experience = employee["em_experience"]
            experiences.append(experience)

        print("Employee Experience Sorting : ", sorted(experiences))

        for employeename in employeedetail.values():
            name = employeename["em_name"]
            names.append(name)

        print("Employee Name Sorting : ", names)
sortingg = SORTING()
sortingg.sorting()

class SERCHING:
    def serching(self):
        employeedetail = loaddata.load_data()
        while True :
            try :
                employeeid = int(input("Enter employee id : ")) 
            except ValueError:
                print("ID entered is not interger")
            break

        if str(employeeid)  in employeedetail :
            print(employeedetail[str(employeeid)])

        else :
            print("ID is not found")
serchingg = SERCHING()
serchingg.serching()

class DEPARTMENTWISEANALYSIS:    
    def department_wise_analysis(self):
        employeedetail = loaddata.load_data()

        employeedepartment = input("Enter employee depatment : ")

        for employee in employeedetail.values() :
            if employee["em_department"] == employeedepartment :
                print(employee)
departmentwiseanalysis = DEPARTMENTWISEANALYSIS()
departmentwiseanalysis.department_wise_analysis()

    
