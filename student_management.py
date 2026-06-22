class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        print("-" * 20)


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self):
        student_id = input("Enter Student ID: ")

        if student_id in self.students:
            print("Student ID already exists!")
            return

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        grade = input("Enter Grade: ")

        self.students[student_id] = Student(student_id, name, age, grade)
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students.values():
            student.display()

    def search_student(self):
        student_id = input("Enter Student ID to search: ")

        if student_id in self.students:
            self.students[student_id].display()
        else:
            print("Student not found.")

    def update_student(self):
        student_id = input("Enter Student ID to update: ")

        if student_id not in self.students:
            print("Student not found.")
            return

        name = input("Enter New Name: ")
        age = int(input("Enter New Age: "))
        grade = input("Enter New Grade: ")

        self.students[student_id].name = name
        self.students[student_id].age = age
        self.students[student_id].grade = grade

        print("Student updated successfully!")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")

        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    def menu(self):
        while True:
            print("\n===== Student Management System =====")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.update_student()
            elif choice == "5":
                self.delete_student()
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")


# Run the system
sms = StudentManagementSystem()
sms.menu()

