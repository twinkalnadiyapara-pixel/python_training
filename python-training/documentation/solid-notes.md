
# SOLID Integration

### 1. Introduction
SOLID is a set of five object-oriented design principles that help
developers create clean, maintainable, flexible, reusable, and
testable software.

The five SOLID principles are:

- Single Responsibility Principle (SRP)
- Open/Closed Principle (OCP)
- Liskov Substitution Principle (LSP)
- Interface Segregation Principle (ISP)
- Dependency Inversion Principle (DIP)

### Single Responsibility Principle (SRP)

- A class should have only one reason to change. it should have a single well defined responsibility.

#### Problem It Tries to Solve

- A class with multiple responsibilities becomes difficult to maintain,
test, and modify.

#### Bad Design Example :

````
    class Employee:
    def add_employee(self):
        print("Employee added")

    def send_email(self):
        print("Email sent")

    def generate_report(self):
        print("Report generated")
````

#### Improved Design

````
    class Employee:
        def add_employee(self):
            print("Employee added")


    class EmailService:
        def send_email(self):
            print("Email sent")


    class ReportGenerator:
        def generate_report(self):
            print("Report generated")
````


### Open/Closed Principle (OCP)

 - A class or module should be open for extension but closed for modification. in simple language, when you want to add a new 
feature think more about creating new classes and modules and less about modifying exisiting classes/modules.

#### Problem It Tries to Solve :

- Adding a new feature should not require modifying existing working code.

#### Bad Design Example :

````
    class Notification:
        def send(self, notification_type):
            if notification_type == "email":
                print("Email sent")
            elif notification_type == "sms":
                print("SMS sent")
````

#### Improved Design :

````
    class Notification:
        def send(self):
            pass


    class EmailNotification(Notification):
        def send(self):
            print("Email sent")


    class SMSNotification(Notification):
        def send(self):
            print("SMS sent")
````
## Liskov Substitution Principle (LSP)

- Any instance of a subclass should be substitutable for an instance of its base class. Simply put, the subclass should behave
in a way that is consistent with the the base class.

#### Problem It Tries to Solve :

It prevents incorrect or inappropriate inheritance relationships.

#### Bad Design Example :

````
    class Bird:
        def fly(self):
            print("Bird is flying")


    class Penguin(Bird):
        def fly(self):
            raise Exception("Penguins cannot fly")
````

#### Improved Design :

````
    class Bird:
        pass


    class FlyingBird(Bird):
        def fly(self):
            print("Bird is flying")


    class Sparrow(FlyingBird):
        pass


    class Penguin(Bird):
        def swim(self):
            print("Penguin is swimming")
````
## Interface Segregation Principle (ISP)

- Instead of creating one large , all-purpose interface, break it into smaller, more specific interfaces so that each class only has
methods relevant to it. A class should only have to implement methods it actually uses.

- A class should not be forced to depend on methods that it does not use.

#### Problem It Tries to Solve :

Large interfaces can force classes to implement unnecessary methods

#### Bad Design Example :

````
    class Notification:
        def send_email(self):
            pass

        def send_sms(self):
            pass

        def send_application(self):
            pass
````

#### Improved Design :

````
    class EmailNotification:
        def send_email(self):
            print("Email sent")


    class SMSNotification:
        def send_sms(self):
            print("SMS sent")


    class ApplicationNotification:
        def send_application(self):
            print("Application notification sent")
````


## Dependency Inversion Principle (DIP)

- All components should depend on abstractions and not on concrete classes. This makes the code more flexible and decoupled.

- High-level modules should not depend directly on low-level modules.

- Both should depend on abstractions.

#### Problem It Tries to Solve

It reduces tight coupling between classes.

#### Bad Design Example :

````
    class EmailService:
        def send(self):
            print("Email sent")


    class NotificationManager:
        def __init__(self):
            self.email = EmailService()

        def notify(self):
            self.email.send()
````

#### Improved Design:

````
    class NotificationService:
        def send(self):
            pass


    class EmailService(NotificationService):
        def send(self):
            print("Email sent")


    class NotificationManager:
        def __init__(self, service):
            self.service = service

        def notify(self):
            self.service.send()
````