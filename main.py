from database import *

def menu():
    print("\nSTUDENT RECORD MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

def main():
    create_table()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter student name: ")
            department = input("Enter department: ")
            level = input("Enter level: ")
            add_student(name, department, level)
            print("Student added successfully!")

        elif choice == "2":
            students = get_students()
            for student in students:
                print(student)

        elif choice == "3":
            student_id = input("Enter student ID: ")
            name = input("Enter new name: ")
            department = input("Enter new department: ")
            level = input("Enter new level: ")
            update_student(student_id, name, department, level)
            print("Student updated successfully!")

        elif choice == "4":
            student_id = input("Enter student ID: ")
            delete_student(student_id)
            print("Student deleted successfully!")

        elif choice == "5":
            print("Exiting system...")
            break

        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
