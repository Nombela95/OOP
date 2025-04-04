# Object-Oriented Programming (OOP) Assignments

## Overview
This project contains two assignments that explore **Object-Oriented Programming (OOP)** concepts in Python.

1️⃣ **Assignment 1: Design Your Own Class** – Create a custom class with attributes, methods, and inheritance.  
2️⃣ **Activity 2: Polymorphism Challenge** – Implement polymorphism with different `move()` behaviors in animals and vehicles.

## Technologies Used
- Python 3

## Assignment 1: Custom Class Design
### Description
This task involves creating a **custom class** representing an object (e.g., a Smartphone, Book, or Superhero).  
The class includes attributes, methods, and demonstrates **inheritance** for reusability.

### Features
- Encapsulation: Uses constructors to initialize objects with unique values.
- Inheritance: A subclass extends the main class, adding extra functionality.

### Example Classes
#### Base Class: `Smartphone`
```python
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def get_info(self):
        return f"{self.brand} {self.model} costs ${self.price}"
```
## Git clone
```
git clone https://github.com/yourusername/oop-assignments.git
cd oop-assignments
```
