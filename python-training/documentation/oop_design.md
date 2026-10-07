
OOP Design — Employee Management System


## Introduction

The purpose of this document is to define the object-oriented design of the Employee Management System before implementation.

The system is a command-line application that manages employee records and performs employee data analysis.




## Identified Entities

The Employee Management System contains different entities, and each entity has a specific responsibility.

###

### The identified classes are:

- ISINTEGER
- ISEMAILVALID
- ISEMAILEXISTS
- ISSALARYINTEGER
- WRITEEMPLOYEEDATAJSON
- ADDEMPLOYEE
- UPDATEEMPLOYEE
- DELETEEMPLOYEE
- SEARCHEMPLOYEE
- DISPLAYALLEMPLOYEE
- EXITEMPLOYEE

###

These classes are responsible for input validation, employee operations, data storage, searching, displaying, and exiting the application.

## Responsibilities


#### ISINTEGER 
The responsibility of ISEMAILVALID is to validate employee email input.

It checks whether the entered email contains basic email characters such as `@` and `.`.

---

### ISEMAILVALID

The responsibility of ISEMAILVALID is to validate employee email input.

It checks whether the entered email contains basic email characters such as `@` and `.`.

---

### ISEMAILEXISTS

The responsibility of ISEMAILEXISTS is to check whether an employee email already exists in the employee data.

This is used to prevent duplicate email addresses.

---

### ISSALARYINTEGER

The responsibility of ISSALARYINTEGER is to validate employee salary input.

It attempts to convert the entered salary into an integer and handles invalid salary input.

---

### WRITEEMPLOYEEDATAJSON

The responsibility of WRITEEMPLOYEEDATAJSON is to save employee data into the JSON file.

It uses Python's `json.dump()` to write the employee data into:

`employee_manager.json`

This class separates file-writing responsibility from employee management operations.

---
### ADDEMPLOYEE

The responsibility of ADDEMPLOYEE is to add a new employee to the system.

It:

1. Gets employee ID.
2. Checks whether the employee ID already exists.
3. Gets employee name.
4. Validates employee email.
5. Checks duplicate email.
6. Gets department.
7. Gets salary.
8. Gets experience.
9. Creates the employee record.
10. Saves the data into the JSON file.

---

### UPDATEEMPLOYEE

The responsibility of UPDATEEMPLOYEE is to update an existing employee record.

It finds an employee using the employee ID and allows the user to change:

- Employee name
- Employee email
- Employee department
- Employee salary
- Employee experience

After updating the record, it saves the updated data into the JSON file.

---

### DELETEEMPLOYEE

The responsibility of DELETEEMPLOYEE is to remove an employee from the employee data.

It asks for an employee ID, checks whether the ID exists, and deletes the corresponding employee record.

---

### SEARCHEMPLOYEE

The responsibility of SEARCHEMPLOYEE is to find an employee using employee ID.

It reads the employee data from the JSON file and displays the employee record if the ID exists.

---

### DISPLAYALLEMPLOYEE

The responsibility of DISPLAYALLEMPLOYEE is to display all employee records.

It reads the employee data from the JSON file and displays the available records.

---

### EXITEMPLOYEE

The responsibility of EXITEMPLOYEE is to handle the exit operation.

It displays a message when the user exits the application.

---


## Relationships

The classes work together to complete employee management operations.

### Main and Employee Operations

The main application provides the menu and calls the appropriate employee operation.

For example:

- Add option → ADDEMPLOYEE
- Update option → UPDATEEMPLOYEE
- Delete option → DELETEEMPLOYEE
- Search option → SEARCHEMPLOYEE
- Display option → DISPLAYALLEMPLOYEE
- Exit option → EXITEMPLOYEE

### Employee Operations and Validation

ADDEMPLOYEE and UPDATEEMPLOYEE use validation classes when collecting employee information.

For example:

`ISINTEGER` is used for employee ID.

`ISEMAILVALID` is used for email validation.

`ISEMAILEXISTS` is used to check duplicate email.

`ISSALARYINTEGER` is used for salary validation.

### Employee Operations and JSON Storage

ADDEMPLOYEE and UPDATEEMPLOYEE use WRITEEMPLOYEEDATAJSON to save employee data.

The JSON file is used as persistent storage.

### Search and Display

SEARCHEMPLOYEE and DISPLAYALLEMPLOYEE read employee data from the JSON file to search or display records.

---
##  Class Design

The application follows an object-oriented approach where different responsibilities are divided into different classes.

### Input Validation Classes


- ISINTEGER
- ISEMAILVALID
- ISEMAILEXISTS
- ISSALARYINTEGER


### Employee Operation Classes

- ADDEMPLOYEE
- UPDATEEMPLOYEE
- DELETEEMPLOYEE
- SEARCHEMPLOYEE
- DISPLAYALLEMPLOYEE
- EXITEMPLOYEE

### Data Storage Class

- WRITEEMPLOYEEDATAJSON

## Expected Interactions

####  Add Employee Interaction
```text
User
 |
ADDEMPLOYEE
 |
 +--> ISINTEGER
 |
 +--> ISEMAILVALID
 |
 +--> ISEMAILEXISTS
 |
 +--> ISSALARYINTEGER
 |
 v
Employee Data
 |
 v
WRITEEMPLOYEEDATAJSON
 |
 v
employee_manager.json
```

#### Update Employee Interaction
```text
User
 |
 v
UPDATEEMPLOYEE
 |
 +--> ISINTEGER
 |
 +--> ISEMAILVALID
 |
 +--> ISEMAILEXISTS
 |
 +--> ISSALARYINTEGER
 |
 v
Updated Employee Data
 |
 v
WRITEEMPLOYEEDATAJSON
 |
 v
employee_manager.json
```

#### Delete Employee Interaction
```text
User
 |
 v
DELETEEMPLOYEE
 |
 v
Employee ID
 |
 v
Check Employee Exists
 |
 +--> Yes --> Delete Employee
 |
 +--> No  --> Display "ID not found"
```

#### Search Employee Interaction
```text
User
 |
 v
SEARCHEMPLOYEE
 |
 v
Enter Employee ID
 |
 v
Read employee_manager.json
 |
 v
Find Employee
 |
 +--> Found     --> Display Employee
 |
 +--> Not Found --> Display "ID is not found"
```

### Display All Employees Interaction
```text
User
 |
 v
DISPLAYALLEMPLOYEE
 |
 v
Read employee_manager.json
 |
 v
Display all employee records
```

## Why the Selected Design Was Chosen

The selected design separates different responsibilities into different classes.

This design was chosen because the Employee Management System contains multiple types of operations such as validation, employee management, searching, displaying, and JSON data storage.

By separating responsibilities:

- Input validation can be changed without changing JSON storage.
- JSON storage can be changed without rewriting validation logic.
- Add, update, delete, and search operations remain separate.
- Each class has a clear purpose.
- The code becomes easier to read and debug.
- Individual responsibilities can be tested independently.
- The application can be extended in the future.