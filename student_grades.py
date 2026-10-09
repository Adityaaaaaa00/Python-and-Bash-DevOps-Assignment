
students = {
    "Aman": "A",
    "Priya": "B",
    "Rahul": "C"
}

while True:
    print("\n--- Student Grades Menu ---")
    print("1. Add a new student")
    print("2. Update an existing student's grade")
    print("3. Display all student grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ").strip()

        if name in students:
            print("Student already exists!")
        else:
            grade = input("Enter grade (A, B, C, D, F): ").strip().upper()

            if grade in ["A", "B", "C", "D", "F"]:
                students[name] = grade
                print("Student added successfully!")
            else:
                print("Invalid grade!")

    elif choice == "2":
        name = input("Enter student name to update: ").strip()

        if name in students:
            grade = input("Enter new grade (A, B, C, D, F): ").strip().upper()

            if grade in ["A", "B", "C", "D", "F"]:
                students[name] = grade
                print("Grade updated successfully!")
            else:
                print("Invalid grade!")
        else:
            print("Student not found!")

    elif choice == "3":
        if students:
            print("\n--- All Student Grades ---")
            for name, grade in students.items():
                print(f"{name}: {grade}")
        else:
            print("No student records available.")

    elif choice == "4":
        print("Exiting Student Grades System.")
        break

    else:
        print("Invalid choice! Please select 1, 2, 3, or 4.")