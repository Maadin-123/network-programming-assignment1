# File: simple_authenticator.py
users = {"admin": "admin123", "student": "net2026", "lecturer": "teach456"}

username = input("Username: ")
password = input("Password: ")

if users.get(username) == password:
    print("Authentication successful")
else:
    print("Authentication failed")