from save_contacts import save_contact_to_file  # Import the function
import os

# List to store contacts
contacts = []

# File name
CONTACTS_FILE = "contacts.txt"

# Function to load contacts from the file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            for line in file:
                name, email, phone, address = line.strip().split(",")
                contacts.append({'Name': name, 'Email': email, 'Phone': phone, 'Address': address})

# Function to save all contacts back to the file (overwrite)
def save_all_contacts():
    with open(CONTACTS_FILE, "w") as file:
        for contact in contacts:
            file.write(f"{contact['Name']},{contact['Email']},{contact['Phone']},{contact['Address']}\n")

# Function to add a contact
def add_contact():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")

    # Check for duplicate phone numbers
    for contact in contacts:
        if contact['Phone'] == phone:
            print("Error: A contact with this phone number already exists.")
            return

    # Create a contact dictionary
    contact = {
        'Name': name,
        'Email': email,
        'Phone': phone,
        'Address': address
    }
    contacts.append(contact)  # Add to in-memory list
    save_contact_to_file(contact)  # Save to file
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\nContacts List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['Name']}, Email: {contact['Email']}, Phone: {contact['Phone']}, Address: {contact['Address']}")

# Function to remove a contact
def remove_contact():
    if not contacts:
        print("No contacts found.")
        return

    phone_to_remove = input("Enter the phone number of the contact to remove: ").strip()
    
    # Find and remove the contact
    for contact in contacts:
        if contact['Phone'] == phone_to_remove:
            contacts.remove(contact)
            save_all_contacts()  # Save updated contacts back to file
            print("Contact removed successfully!")
            return

    print("Error: Contact not found.")

# Main program
def main():
    load_contacts()  # Load existing contacts from the file at startup
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Exit")

        choice = input("Choose an option (1/2/3/4): ").strip()
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            remove_contact()
        elif choice == '4':
            print("Thanks for using contacts!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
