import json
import os

class Student:
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "grade": self.grade
        }


class StudentManager:
    FILE_NAME = "students.json"

    def __init__(self):
        self.students = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)
                self.students = [Student(**s) for s in data]

    def save_data(self):
        with open(self.FILE_NAME, "w") as file:
            json.dump([s.to_dict() for s in self.students], file, indent=4)

    def is_unique_id(self, student_id):
        return all(s.id != student_id for s in self.students)

    def add_student(self, student_id, name, grade):
        if not self.is_unique_id(student_id):
            print("Error: Student ID already exists.")
            return
        self.students.append(Student(student_id, name, grade))
        self.save_data()
        print("Student added successfully.")

    def update_student(self, student_id, name, grade):
        for s in self.students:
            if s.id == student_id:
                s.name = name
                s.grade = grade
                self.save_data()
                print("Student updated successfully.")
                return
        print("Student not found.")

    def delete_student(self, student_id):
        for s in self.students:
            if s.id == student_id:
                self.students.remove(s)
                self.save_data()
                print("Student deleted successfully.")
                return
        print("Student not found.")

    def list_students(self):
        if not self.students:
            print("No student records available.")
            return

        print("\n{:<10} {:<20} {:<10}".format("ID", "Name", "Grade"))
        print("-" * 40)
        for s in self.students:
            print("{:<10} {:<20} {:<10}".format(s.id, s.name, s.grade))


def main():
    manager = StudentManager()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. List Students")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            manager.add_student(
                input("ID: "),
                input("Name: "),
                input("Grade: ")
            )
        elif choice == "2":
            manager.update_student(
                input("ID: "),
                input("New Name: "),
                input("New Grade: ")
            )
        elif choice == "3":
            manager.delete_student(input("ID: "))
        elif choice == "4":
            manager.list_students()
        elif choice == "5":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()