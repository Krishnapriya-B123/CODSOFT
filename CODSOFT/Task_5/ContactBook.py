# CONTACT BOOK 

contacts = {}

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    print("Contact added successfully!\n")


def view_contacts():
    if not contacts:
        print("No contacts available.\n")
        return

    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['Phone']}")
    print()


def search_contact():
    search = input("Enter name or phone number to search: ")

    found = False
    for name, details in contacts.items():
        if search.lower() == name.lower() or search == details["Phone"]:
            print("\nContact Found:")
            print(f"Name: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}\n")
            found = True

    if not found:
        print("Contact not found.\n")


def update_contact():
    name = input("Enter the name of the contact to update: ")

    if name in contacts:
        print("Enter new details:")
        contacts[name]["Phone"] = input("New phone number: ")
        contacts[name]["Email"] = input("New email: ")
        contacts[name]["Address"] = input("New address: ")
        print("Contact updated successfully!\n")
    else:
        print("Contact not found.\n")


def delete_contact():
    name = input("Enter the name of the contact to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!\n")
    else:
        print("Contact not found.\n")


# Main menu
while True:
    print("===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Thank you for using Contact Book!")
        break
    else:
        print("Invalid choice. Please try again.\n")