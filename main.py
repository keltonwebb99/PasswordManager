# Import necessary libraries
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin SDK and connect to the Firestore database
cred = credentials.Certificate("passwordmanager-b8fb3-firebase-adminsdk-enr8y-26bb05693a.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Specify the name of the collection in the Firestore database
collection_name = "passwords"

# Function to add a password to the database
def add_password():
    document_name = input("Enter a document name: ")
    password = input("Enter the password: ")
    username = input("Enter the username: ")
    
    # Create a dictionary with password and username data
    password_data = {
        "password": password,
        "username": username
    }
    
    # Add the password data to the specified document in the collection
    db.collection(collection_name).document(document_name).set(password_data)
    print("Password added successfully!")

# Function to retrieve a password from the database
def get_password():
    document_name = input("Enter the document name: ")
    
    # Get the document reference from the specified document in the collection
    doc_ref = db.collection(collection_name).document(document_name)
    
    # Get the document data if it exists and print the password and username
    doc = doc_ref.get()
    if doc.exists:
        password_data = doc.to_dict()
        print("Password:", password_data.get("password"))
        print("Username:", password_data.get("username"))
    else:
        print("Password not found.")

# Function to update a password in the database
def update_password():
    document_name = input("Enter the document name: ")
    new_password = input("Enter the new password: ")
    
    # Get the document reference from the specified document in the collection
    doc_ref = db.collection(collection_name).document(document_name)
    
    # Update the password field in the document with the new password
    doc_ref.update({"password": new_password})
    print("Password updated successfully!")

# Function to delete a password from the database
def delete_password():
    document_name = input("Enter the document name: ")
    
    # Get the document reference from the specified document in the collection
    doc_ref = db.collection(collection_name).document(document_name)
    
    # Check if the document exists and delete it if it does
    doc = doc_ref.get()
    if doc.exists:
        doc_ref.delete()
        print("Password deleted successfully!")
    else:
        print("Password not found.")

# Main program loop
while True:
    # Print menu options and get user's choice
    print("Select an option:")
    print("1. Add a password")
    print("2. Retrieve a password")
    print("3. Update a password")
    print("4. Delete a password")
    print("5. Exit")
    choice = input("Enter your choice: ")

    # Execute the corresponding function based on the user's choice
    if choice == "1":
        add_password()
    elif choice == "2":
        get_password()
    elif choice == "3":
        update_password()
    elif choice == "4":
        delete_password()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
