import json
from datetime import datetime

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}

    def enroll(self, course_name):
        if course_name not in self.courses:
            self.courses[course_name] = None  # None means no grade yet

    def record_grade(self, course_name, grade):
        if course_name in self.courses:
            self.courses[course_name] = grade
        else:
            print(f"[ERROR] ❌ Student not enrolled in {course_name}")

    def get_info(self):
        return {
            'student_id': self.student_id,
            'name': self.name,
            'courses': self.courses
        }

class StudentManagementSystem:
    def __init__(self, filename='students_data.json'):
        self.filename = filename
        self.students = {}
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                for student_id, student_info in data.items():
                    student = Student(student_id, student_info['name'])
                    student.courses = student_info['courses']
                    self.students[student_id] = student
        except FileNotFoundError:
            self.students = {}

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump({student_id: student.get_info() for student_id, student in self.students.items()}, file, indent=4)

    def add_student(self, student_id, name):
        if student_id not in self.students:
            student = Student(student_id, name)
            self.students[student_id] = student
            self.save_data()
            print(f"\n[INFO] 🎓 Student '{name}' has been successfully added!")
        else:
            print(f"[ERROR] ❌ Student ID '{student_id}' already exists.")

    def enroll_student(self, student_id, course_name):
        if student_id in self.students:
            self.students[student_id].enroll(course_name)
            self.save_data()
            print(f"\n[INFO] ✅ Student '{student_id}' is now enrolled in '{course_name}'.")
        else:
            print(f"[ERROR] ❌ Student ID '{student_id}' not found.")

    def record_student_grade(self, student_id, course_name, grade):
        if student_id in self.students:
            self.students[student_id].record_grade(course_name, grade)
            self.save_data()
            print(f"\n[INFO] 📚 Grade '{grade}' has been recorded for '{course_name}'.")
        else:
            print(f"[ERROR] ❌ Student ID '{student_id}' not found.")

    def view_student_records(self):
        if not self.students:
            print("\n[INFO] 📝 No student records available.")
            return

        print("\n--- Student Records ---")
        for student_id, student in self.students.items():
            print(f"\n** Student ID: {student_id} **")
            print(f"Name: {student.name}")
            print("Courses:")
            for course, grade in student.courses.items():
                grade_display = grade if grade is not None else "Not graded yet"
                print(f"  - {course}: {grade_display}")
        print("\n[INFO] 🎉 All records displayed successfully!")

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            self.save_data()
            print(f"\n[INFO] ✅ Student ID '{student_id}' has been removed.")
        else:
            print(f"[ERROR] ❌ Student ID '{student_id}' not found.")

    def update_student_name(self, student_id, new_name):
        if student_id in self.students:
            self.students[student_id].name = new_name
            self.save_data()
            print(f"\n[INFO] ✅ Student ID '{student_id}' name has been updated to '{new_name}'.")
        else:
            print(f"[ERROR] ❌ Student ID '{student_id}' not found.")

    def view_course_enrollment(self, course_name):
        enrolled_students = [student.name for student in self.students.values() if course_name in student.courses]
        if enrolled_students:
            print(f"\n[INFO] Students enrolled in '{course_name}':")
            for name in enrolled_students:
                print(f"  - {name}")
        else:
            print(f"\n[INFO] No students are enrolled in '{course_name}'.")

def print_header():
    print("Student Management System")

def main():
    print_header()
    system = StudentManagementSystem()
    while True:
        print("\nMain Menu")
        print("1. Add Student")
        print("2. Enroll Student in Course")
        print("3. Record Student Grade")
        print("4. View Student Records")
        print("5. Remove Student")
        print("6. Update Student Name")
        print("7. View Course Enrollment")
        print("8. Exit")

        choice = input("Select an option (1-8): ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            system.add_student(student_id, name)

        elif choice == '2':
            student_id = input("Enter student ID: ")
            course_name = input("Enter course name: ")
            system.enroll_student(student_id, course_name)

        elif choice == '3':
            student_id = input("Enter student ID: ")
            course_name = input("Enter course name: ")
            grade = input("Enter grade: ")
            system.record_student_grade(student_id, course_name, grade)

        elif choice == '4':
            system.view_student_records()

        elif choice == '5':
            student_id = input("Enter student ID to remove: ")
            system.remove_student(student_id)

        elif choice == '6':
            student_id = input("Enter student ID: ")
            new_name = input("Enter new student name: ")
            system.update_student_name(student_id, new_name)

        elif choice == '7':
            course_name = input("Enter course name to view enrollment: ")
            system.view_course_enrollment(course_name)

        elif choice == '8':
            print("Goodbye! 👋")
            break

        else:
            print("[ERROR] ❌ Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
