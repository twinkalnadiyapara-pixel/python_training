from Employee_Operations import employee_manager as emp

while True :
    print("________ System Management System ________")

    print("1. Add Employee :")
    print("2. Update Employee :")
    print("3. Delete Employee :")
    print("4. Search Employee :")
    print("5. Display All Employee :")
    print("6. Exit...")

    Choice = int(input("Enter Your Choice : "))

    match Choice:
        case 1:
            emp.addemployeedata.add_employee()
        case 2:
            emp.updateemployeedata.update_employee()
        case 3:
            emp.deleteemployeedata.delete_employee()
        case 4:
            emp.searchemployeedata.search_employee()
        case 5:
            emp.displayallemployeedata.display_all_employees()
        case 6:
            emp.exitemployeedata.exit_employee()
            break
        case _:
            print("Please select valid value")
        