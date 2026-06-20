# File: protected_page_simulation.py
users = {"admin": "admin123", "student": "net2026", "lecturer": "teach456"}

u = input("Username: ")
p = input("Password: ")

if users.get(u) == p:
    print("Welcome to internal portal.")
    print("1. Lecture notes")
    print("2. Lab exercises") 
    print("3. Assignment submissions")
else:
    print("Access denied.")