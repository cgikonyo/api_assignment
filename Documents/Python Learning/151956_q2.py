class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Added grade {grade} for '{assignment_name}' to {self.name}'s record.")

    def display_grades(self):
        print(f"Grades for {self.name}:")
        if self.assignments:
            for assignment, grade in self.assignments.items():
                print(f"- {assignment}: {grade}")
        else:
            print("No grades available.")

class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} has been added to the course '{self.course_name}'.")

    def assign_grade(self, student_id, assignment_name, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_assignment(assignment_name, grade)
        else:
            print(f"No student found with ID {student_id}.")

    def display_all_students_grades(self):
        print(f"Grades for all students in '{self.course_name}':")
        for student in self.students:
            student.display_grades()

# Interactive code
def main():
    # Create an instructor for a course
    instructor = Instructor("Dr. Smith", "Python Programming 101")

    # Add students interactively
    student1 = Student("Alice", 1)
    student2 = Student("Bob", 2)
    
    instructor.add_student(student1)  # Add Alice to the course
    instructor.add_student(student2)  # Add Bob to the course

    # Assign grades interactively
    instructor.assign_grade(1, "Assignment 1", 85)  # Grade Alice on Assignment 1
    instructor.assign_grade(2, "Assignment 1", 90)  # Grade Bob on Assignment 1
    instructor.assign_grade(1, "Assignment 2", 95)  # Grade Alice on Assignment 2

    # Display all students and their grades
    instructor.display_all_students_grades()

main()