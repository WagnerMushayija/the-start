import getpass
from patient import Patient

def register():
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")
    patient = Patient(username)
    patient.register(password)

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    return Patient.login(username, password)
