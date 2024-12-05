# Function to save a single contact to the file
def save_contact_to_file(contact):
    with open("contacts.txt", "a") as file:  # Open in append mode
        file.write(f"{contact['Name']},{contact['Email']},{contact['Phone']},{contact['Address']}\n")
        print("Contact saved to file successfully!")
