
inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

while True:
    print()
    print("===== INVENTORY CONTROL SYSTEM =====")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        print()
        print("--- Current Inventory ---")
        for item in inventory:
            print(item)

    elif choice == 2:
        item = input("Enter item name to add: ")

        if item not in inventory:
            inventory.append(item)
            print("SUCCESS:", item, "added to inventory.")
        else:
            print("Item already exists in inventory.")

    elif choice == 3:
        item = input("Enter item name to remove: ")

        if item in inventory:
            inventory.remove(item)
            print("SUCCESS:", item, "removed from inventory.")
        else:
            print("ERROR: Item not found in inventory.")

    elif choice == 4:
        inventory.sort()
        print("SUCCESS: Inventory sorted alphabetically.")
        print("--- Updated Inventory ---")
        for item in inventory:
            print(item)

    elif choice == 5:
        print("Exiting Inventory Control System. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
