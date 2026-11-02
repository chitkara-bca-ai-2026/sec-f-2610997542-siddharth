
library_books = [
    ("Python Crash Course", "Eric Matthes", "Programming"),
    ("Data Structures and Algorithms", "Miller", "Programming"),
    ("Automate the Boring Stuff with Python", "Al Sweigart", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "AI"),
    ("The C++ Programming Language", "Bjarne Stroustrup", "Programming"),
    ("Cyber Security Basics", "Patrick Engebretson", "Cybersecurity")
]

library_categories = {"AI", "Data Science", "Programming", "Software Engineering"}
student_wishlist = {"AI", "Cloud Computing", "Robotics", "Cybersecurity"}

while True:
    print()
    print("========================================")
    print("       LIBRARY BOOK & CATEGORY MANAGER")
    print("========================================")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print()
        print("--- Current Library Catalog ---")

        for book in library_books:
            print("Book:", book[0])
            print("Author:", book[1])
            print("Category:", book[2])
            print()

        print("Total Books:", len(library_books))

    elif choice == "2":
        print()
        print("--- Add New Book Record ---")

        title = input("Enter book title: ")
        author = input("Enter author name: ")
        category = input("Enter category: ")

        if title != "" and author != "" and category != "":
            library_books.append((title, author, category))
            library_categories.add(category)

            print("SUCCESS:", title, "added to catalog.")
            print("Category updated:", category)
        else:
            print("ERROR: All fields are required.")

    elif choice == "3":
        print()
        print("--- Unique Categories Available in Library ---")

        for category in sorted(library_categories):
            print("-", category)

        print("Total Unique Genres:", len(library_categories))

    elif choice == "4":
        print()
        print("--- Add to Student Wishlist ---")

        category = input("Enter category to add: ")

        if category != "":
            student_wishlist.add(category)
            print("SUCCESS:", category, "added to student wishlist.")
        else:
            print("ERROR: Category cannot be empty.")

    elif choice == "5":
        print()
        print("========== CATEGORY GAP ANALYSIS ==========")

        print("Library Holdings (Set):", library_categories)
        print("Student Wishlist (Set):", student_wishlist)

        intersection = library_categories.intersection(student_wishlist)
        difference = student_wishlist.difference(library_categories)
        union = library_categories.union(student_wishlist)

        print()
        print("1. Intersection (Books Available):")
        print(intersection)

        print()
        print("2. Difference (Wishlist Categories Not Available):")
        print(difference)

        print()
        print("3. Union (All Categories Combined):")
        print(union)

    elif choice == "6":
        print()
        print("Thank you for using the Library Manager!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 6.")
