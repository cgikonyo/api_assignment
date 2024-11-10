class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: ${self.salary:.2f}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Updated salary for {self.name} to ${self.salary:.2f}")

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added {employee.name} to the {self.department_name} department.")

    def total_salary_expenditure(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for {self.department_name}: ${total_salary:.2f}")
        return total_salary

    def display_all_employees(self):
        print(f"Employees in {self.department_name} department:")
        if self.employees:
            for employee in self.employees:
                employee.display_details()
        else:
            print("No employees in this department.")

# Interactive code
def main():
    # Create a department
    department = Department("Engineering")

    # Add employees interactively
    emp1 = Employee("Alice", 101, 60000)
    emp2 = Employee("Bob", 102, 75000)
    
    department.add_employee(emp1)  # Add Alice to Engineering
    department.add_employee(emp2)  # Add Bob to Engineering

    # Display all employees in the department
    department.display_all_employees()

    # Update salary of an employee
    emp1.update_salary(65000)

    # Calculate and display total salary expenditure
    department.total_salary_expenditure()

main()