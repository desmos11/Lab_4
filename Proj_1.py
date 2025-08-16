#Create a CLI (Command Line Interface) contact book that allows users to:
#● Add a new contact (append to file)
#● View all contacts (read from file)
#● Search for a contact (read and filter)
#● Handle file-related exceptions (e.g., file not found)
#File Used:
#contacts.txt (stores contact info: Name, Phone)

def add_contacts():
    try:
        with open("contacts.txt", "a") as c:
            e = int(input("How many extra contacts do you want to add: "))
            for i in range(e):
                N = input("Enter their name: ")
                P = input("Enter their phone number: ")  # keep as string
                c.write(f"{i+1}\t{N}\t{P}\n")
        print("Contacts added successfully!")
    except Exception as W:
        print(f"An error occurred: {W}")


def view_Contacts():
    try:
        with open("contacts.txt", "r") as c:
            print(c.read())
    except Exception as W:
        print(f"An error occurred: {W}")



def search_contacts():
    try:
        with open("contacts.txt", "r") as c:
            name = input("Enter the name of the contact you want to search: ")
            found = False
            for line in c:
                if name.lower() in line.lower():
                    print(line.strip())
                    found = True
            if not found:
                print("Contact not found.")
    except FileNotFoundError:
        print("The contacts file does not exist. Please add contacts first.") 

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_contacts()
        elif choice == '2':
            view_Contacts()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  





    





