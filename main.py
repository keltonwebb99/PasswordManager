import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("passwordmanager-b8fb3-firebase-adminsdk-enr8y-26bb05693a.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

collection_name = "passwords"

def add_password():
    document_name = input("Enter a document name: ")
    password = input("Enter the password: ")
    username = input("Enter the username: ")
    password_data = {
        "password": password,
        "username": username
    }
    db.collection(collection_name).document(document_name).set(password_data)
    print("Password added successfully!")

def get_password():
    document_name = input("Enter the document name: ")
    doc_ref = db.collection(collection_name).document(document_name)
    doc = doc_ref.get()
    if doc.exists:
        password_data = doc.to_dict()
        print("Password:", password_data.get("password"))
        print("Username:", password_data.get("username"))
    else:
        print("Password not found.")

def update_password():
    document_name = input("Enter the document name: ")
    new_password = input("Enter the new password: ")
    doc_ref = db.collection(collection_name).document(document_name)
    doc_ref.update({"password": new_password})
    print("Password updated successfully!")

def delete_password():
    document_name = input("Enter the document name: ")
    doc_ref = db.collection(collection_name).document(document_name)
    doc = doc_ref.get()
    if doc.exists:
        doc_ref.delete()
        print("Password deleted successfully!")
    else:
        print("Password not found.")

# Main program loop
while True:
    print("Select an option:")
    print("1. Add a password")
    print("2. Retrieve a password")
    print("3. Update a password")
    print("4. Delete a password")
    print("5. Exit")
    choice = input("Enter your choice: ")

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

