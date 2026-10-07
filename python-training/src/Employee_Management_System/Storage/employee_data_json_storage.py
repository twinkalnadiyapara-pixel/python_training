import json

class WRITEEMPLOYEEDATAJSON:

    def __init__(self):
        self.filename = (
            "D:/python-training/src/Employee_Management_System/Data_Json/employee_manager.json"
        )

    def write_employeedata_json(self, employeedetail):
        with open(self.filename,"w") as f :
            json.dump(employeedetail , f , indent=4)

writeemployeedatajson = WRITEEMPLOYEEDATAJSON()