# Simple Contact Book
contacts = []
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    print("✅ Contact Added Successfully!")
def view_contacts():
    if not contacts:
        print("No contacts found")
    else:
        print("\n Contact List:")
        for i, c in enumerate(contacts, start=1):
            print(f"{i}. Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
def search_contact():
    name = input("Enter name to search: ")
    found = False

    for c in contacts:
        if c["name"].lower() == name.lower():
            print("Contact Found:")
            print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
            found = True

    if not found:
        print("Contact not found")
def delete_contact():
    name = input("Enter name to delete: ")

    for c in contacts:
        if c["name"].lower() == name.lower():
            contacts.remove(c)
            print("Contact Deleted")
            return

    print("Contact not found")
# Main menu
while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print(" Exiting...")
        break
    else:
        print("Invalid choice, try again!")