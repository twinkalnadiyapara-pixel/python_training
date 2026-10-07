import json

class READDATA:
    def read_data(self):
        with open("D:/python-training/src/Employee_Management_System/Data_Json/employee_manager.json","r") as f :
            return json.load(f)

readdata = READDATA()
readdata.read_data()


class EXPERIENCEBONUS:
    def experience_donus(self):
        employee_data = readdata.read_data()

        for employee in employee_data.values():
            if employee["em_salary"] >= 20000 :
                print("not eligible for Bouns")
            else :
                if employee["em_experience"] < 5 :
                    bouns = employee["em_salary"] * 0 / 100
                    print(f"Your Bouns is {bouns}")
                    total_amount = employee["em_salary"] + bouns
                    print(f"So, the total amount of your bonus and salary...{total_amount}")
                    
                elif employee["em_experience"] >= 5 :
                    bouns = employee["em_salary"] * 5 / 100
                    print(f"Your Bouns is {bouns}")
                    total_amount = employee["em_salary"] + bouns
                    print(f"So, the total amount of your bonus and salary...{total_amount}")

                elif employee["em_exprience"] >= 10 :
                    bouns = 15000 * 10 / 100
                    print(f"Your Bouns is {bouns}")
                    total_amount = employee["em_salary"] + bouns
                    print(f"So, the total amount of your bonus and salary...{total_amount}")
            

experiencebonus = EXPERIENCEBONUS()
experiencebonus.experience_donus()