class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    
    def display_info(self):
        return f"Employee: {self.name} (ID: {self.emp_id})"


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []  # Aggregation: Department contains Employees
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def remove_employee(self, emp_id):
        for i, emp in enumerate(self.employees):
            if emp.emp_id == emp_id:
                return self.employees.pop(i)
        return None
    
    def display_employees(self):
        print(f"Department: {self.name}")
        if not self.employees:
            print("  No employees")
        else:
            for emp in self.employees:
                print(f"  {emp.display_info()}")


if __name__ == "__main__":
    # Create employees (exist independently)
    emp1 = Employee("John Doe", 101)
    emp2 = Employee("Jane Smith", 102)
    emp3 = Employee("Alice Johnson", 103)
    
    # Print employee info
    print(emp1.display_info())
    print(emp2.display_info())
    print(emp3.display_info())
    
    print("\n" + "-" * 40 + "\n")
    
    # Create departments
    hr_dept = Department("Human Resources")
    it_dept = Department("Information Technology")
    
    # Add employees to departments
    hr_dept.add_employee(emp1)
    it_dept.add_employee(emp2)
    it_dept.add_employee(emp3)
    
    # Display department employees
    hr_dept.display_employees()
    print()
    it_dept.display_employees()
    
    print("\n" + "-" * 40 + "\n")
    
    # Move an employee from IT to HR
    print("Moving Alice from IT to HR:")
    employee = it_dept.remove_employee(103)
    if employee:
        hr_dept.add_employee(employee)
    
    # Display updated departments
    hr_dept.display_employees()
    print()
    it_dept.display_employees()
    
    # Employees continue to exist even if not in any department
    print("\nEmployee still exists independently:")
    print(emp3.display_info())
