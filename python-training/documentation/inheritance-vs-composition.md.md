
# Inheritance vs Composition



##  1. Introduction

Inheritance and composition are two core object-oriented programming techniques used to reuse code and establish relationships between types.
##  2. What is Inheritance?

when one class(child / derived) derives the properties & methods of another class(parent / base).

A process by which one class can accquire the properties of another class.
___

#### Base class or parentes : 
new class are created from exisiting class that exisiting class is called parent class.
___

#### derived class or child class or sub class :
new classes are created from existing class that new class is called child class.

___
## 3. Inheritance Relationship

- This relationship represents an “is-a” hierarchy.

- Reuses existing functionality by Inheriting from the parent classes

- Less flexible changes in the parent class affect all subclasses

- Leads to tight coupling between parent and child

- Can result an complex hierarchies that hard to extend and modify


#### Python implementation 

````
class ABC():

    def hello(self):
        print("HELOO.....")     
class XYZ(ABC):
    def __init__(self, name):
        self.name = name
xyz1 = XYZ("abcdefgh")
xyz1.hello()
````
## What is Composition ?

- relationship one or other class. data use one class to other class

- By using Class Name or by creating object we can access members of one class inside another class nothing but composition.The main advantage of Has-A Relationship is code Reusability 




## Composition Relationship

- This relationship represents an “has-a” hierarchy.

- Reuses functionality by delegating tasks to other objects.

- More flexible component can be swapped easily.

- Looser coupling making the system more modular.

- components can be added or removed easily without affecting the entire system.

#### Python implementation 
````
class Student():
    def hello(self):
		print("hello student")
class Detail():
		def __init__(self):
			self.d1 = Student() #(object_name=d1)
		def subject(self):
			print("which subject we study")
			self.d1.hello()
s1 = Detail()
s1.subject()
````
## Features Inheritance & Composition

| Feature | Inheritance | Composition |
|---------|-------------|-------------|
| Relationship | IS-A | HAS-A |
| Coupling | Higher | Lower |
| Reusability | Through parent-child relationship | Through object combination |
| Flexibility | Less flexible | More flexible |
| Dependency | Child depends on parent | Objects can be replaced independently |
## Advantages & Disadvantages of Inheritance 

#### Advantages :

- Code reusability
- Extensibility
- Maintenance
- Organization

####  Disadvantages :

- Tight coupling
- Fragile base class
- Increased complexity
- Inflexibility
- Unused code/memory
##  Advantages & Disadvantages  of Composition

#### Advantages :

- Loose Coupling
- High Flexibility
- Better Reusability
- Easier Unit Testing
- Avoids Fragile Base Class Problem

#### Disadvantages :

- Increased Boilerplate Code
- More Classes
- Complex Lifecycle Management
- Steeper Initial Design Effort
