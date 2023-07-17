import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("passwordmanager-b8fb3-firebase-adminsdk-enr8y-26bb05693a.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

collection_name = "passwords"
document_name = "user1"

def add_password(password, username):
    password_data = {
        "password": password,
        "username": username
    }
    db.collection(collection_name).document(document_name).set(password_data)


def get_password():
    doc_ref = db.collection(collection_name).document(document_name)
    doc = doc_ref.get()
    password_data = doc.to_dict()
    return password_data.get("password")


def update_password(new_password):
    doc_ref = db.collection(collection_name).document(document_name)
    doc_ref.update({"password": new_password})


def delete_password():
    db.collection(collection_name).document(document_name).delete()
