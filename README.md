# Overview

I developed this project as a software engineer to learn and improve my skills. The software I created is a password manager that securely stores and retrieves passwords using a cloud database.

With this program, you can easily add, retrieve, update, and delete passwords. It provides a simple and user-friendly interface where you can interact with the software through commands in the terminal. This makes it convenient for managing your passwords.

The main purpose of this software is to help you manage your passwords securely. By using a cloud database, your passwords are stored remotely and can be accessed from anywhere while keeping your data safe.


[Software Demo Video](http://youtube.link.goes.here)

# Cloud Database

For this project, I used Firestore, which is a cloud-based database provided by Google Firebase. Firestore offers scalability, real-time updates, and strong security features, making it a great choice for storing sensitive data like passwords.

The database structure is straightforward. It consists of a collection called "passwords" where each document represents a password entry. Each document has fields like "password" and "username" to store the necessary information securely.

# Development Environment

I developed the software using Python, a popular programming language. To interact with the Firestore database, I utilized the Firebase Admin SDK for Python. For coding and testing, I used Visual Studio Code, a user-friendly code editor.

# Useful Websites

Throughout the project, I found the following websites helpful:

- [Firebase Documentation](https://firebase.google.com/docs)
- [Python Documentation](https://docs.python.org/3/)

# Future Work

While the current version of the password manager software meets the basic requirements, there are areas for improvement. Some future enhancements include:

- Adding user authentication to ensure only authorized users can access the password manager.
- Improving the user interface to make it more interactive and user-friendly.
- Implementing additional features like password strength evaluation, password generation, and organizing passwords into categories.
- Enhancing error handling and implementing proper exception handling mechanisms.
