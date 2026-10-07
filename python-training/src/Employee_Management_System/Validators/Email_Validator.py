
employeedetail = {}

class ISEMAILVALID:
    def is_email_valid(self):
        while True :
        
                employeeemail = input("Enter employee email : ")
        
                if "@" in employeeemail and "." in employeeemail:
                    return employeeemail
                
                print("Please enter a valid email.")
isemailvalid = ISEMAILVALID()

class ISEMAILEXISTS:
    def is_email_exists(employeeemail, self):
        for employee in employeedetail.values():
                    if employee["em_email"] == employeedetail:
                        return True
                    return False
isemailexists = ISEMAILEXISTS()