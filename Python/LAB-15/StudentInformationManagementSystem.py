
students = {
    101: {
        "Name": "Aman",
        "Branch": "BCA AI",
        "Semester": 1,
        "Marks": [85, 90, 78]
    },
    102: {
        "Name": "Riya",
        "Branch": "BCA AI",
        "Semester": 2,
        "Marks": [88, 92, 80]
    },
    103: {
        "Name": "Karan",
        "Branch": "BCA AI",
        "Semester": 1,
        "Marks": [70, 75, 82]
    }
}

while True:
    print()
    print("========================================")
    print(" STUDENT INFORMATION MANAGEMENT SYSTEM")
    print("========================================")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        print()
        print("--- Enrolled Student Records ---")

        for roll, details in students.items():
            print("Roll No:", roll, "| Name:", details["Name"],
                  "| Branch:", details["Branch"])
            print("Semester:", details["Semester"],
                  "| Marks:", details["Marks"])

        print("Total Enrolled Students:", len(students))

    elif choice == "2":
        roll = int(input("Enter Roll Number to search: "))

        if roll in students:
            details = students[roll]
            print("Student Found!")
            print("Roll No:", roll)
            print("Name:", details["Name"])
            print("Branch:", details["Branch"])
            print("Semester:", details["Semester"])
            print("Marks:", details["Marks"])
        else:
            print("ERROR: Student not found.")

    elif choice == "3":
        roll = int(input("Enter Roll Number: "))

        if roll in students:
            print("ERROR: Roll Number already exists.")
        elif roll <= 0:
            print("ERROR: Roll Number must be positive.")
        else:
            name = input("Enter Student Name: ")
            branch = input("Enter Branch: ")
            semester = int(input("Enter Semester (1-8): "))

            if name == "" or branch == "" or semester < 1 or semester > 8:
                print("ERROR: Invalid student details.")
            else:
                marks = []

                for i in range(1, 4):
                    mark = int(input("Enter marks for Subject " + str(i) + ": "))

                    if mark < 0 or mark > 100:
                        print("ERROR: Marks must be between 0 and 100.")
                        break

                    marks.append(mark)

                if len(marks) == 3:
                    students[roll] = {
                        "Name": name,
                        "Branch": branch,
                        "Semester": semester,
                        "Marks": marks
                    }
                    print("SUCCESS: Student registered successfully.")

    elif choice == "4":
        roll = int(input("Enter Roll Number to update: "))

        if roll in students:
            print("1. Update Name")
            print("2. Update Branch")
            print("3. Update Semester")

            field = input("Choose field to update (1-3): ")

            if field == "1":
                name = input("Enter new name: ")
                if name != "":
                    students[roll]["Name"] = name
                    print("SUCCESS: Name updated.")

            elif field == "2":
                branch = input("Enter new branch: ")
                if branch != "":
                    students[roll]["Branch"] = branch
                    print("SUCCESS: Branch updated.")

            elif field == "3":
                semester = int(input("Enter new semester (1-8): "))
                if 1 <= semester <= 8:
                    students[roll]["Semester"] = semester
                    print("SUCCESS: Semester updated.")
                else:
                    print("ERROR: Invalid semester.")

            else:
                print("Invalid field choice.")
        else:
            print("ERROR: Student not found.")

    elif choice == "5":
        roll = int(input("Enter Roll Number: "))

        if roll in students:
            details = students[roll]
            marks = details["Marks"]
            total = sum(marks)
            average = total / len(marks)

            if average >= 40:
                result = "PASS"
            else:
                result = "FAIL"

            print()
            print("========== ACADEMIC REPORT ==========")
            print("Student Name:", details["Name"])
            print("Roll Number:", roll)
            print("Subject Marks:", marks)
            print("Total Marks:", total, "/", len(marks) * 100)
            print("Average Marks:", round(average, 2))
            print("Final Result:", result)
            print("=====================================")
        else:
            print("ERROR: Student not found.")

    elif choice == "6":
        roll = int(input("Enter Roll Number to delete: "))

        if roll in students:
            del students[roll]
            print("SUCCESS: Student record deleted.")
        else:
            print("ERROR: Student not found.")

    elif choice == "7":
        print("Thank you for using Student Information System!")
        break

    else:
        print("Invalid choice! Enter a number from 1 to 7.")
