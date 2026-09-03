    print("3. Search for a Student")
    print("4. Display All Records (Sorted)")
    print("5. Count Total Enrollments")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enrollment_id = int(input("Enter Enrollment ID: "))
        student_name = input("Enter Student Name: ")

        root = avl.insert(root, enrollment_id, student_name)
        print("Record inserted successfully.")

    elif choice == 2:
        enrollment_id = int(input("Enter Enrollment ID to delete: "))

        if avl.search(root, enrollment_id):
            root = avl.delete(root, enrollment_id)
            print("Record deleted successfully.")
        else:
            print("Enrollment ID not found.")

    elif choice == 3:
        enrollment_id = int(input("Enter Enrollment ID to search: "))

        result = avl.search(root, enrollment_id)

        if result:
            print("Student Found!")
            print("Enrollment ID :", result.enrollment_id)
            print("Student Name  :", result.student_name)
        else:
            print("Student not found.")

    elif choice == 4:
        print("\nEnrollment Records (Sorted by Enrollment ID):")

        if root is None:
            print("No records available.")
        else:
            avl.inorder(root)

    elif choice == 5:
        print("Total Enrollments:", avl.count(root))

    elif choice == 6:
        print("Program terminated.")
        break

    else:
        print("Invalid choice!")

