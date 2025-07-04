import json
import os

# ---------------- Custom Exceptions ----------------
class SecurityError(Exception):
    def __init__(self, message):
        super().__init__(message)
        print(" Security Alert:", message)
        if self.check_already_login():
            self.send_message()

    def check_already_login(self):
        return True

    def send_message(self):
        print(" Notification sent: Suspicious login detected!")

class LoginError(Exception):
    def __init__(self, message):
        super().__init__(message)
        print(" Login Error:", message)

# ---------------- Google Class ----------------
class Google:
    def __init__(self, name, email, password, device):
        self.name = name
        self.email = email
        self.__password = password
        self.device = device

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.__password,
            "device": self.device
        }

    def login(self, email_input, password_input, device_input):
        if self.email != email_input or self.__password != password_input:
            raise LoginError("Incorrect email or password.")
        if self.device != device_input:
            raise SecurityError("Login from unknown device detected.")
        print(f" Welcome back, {self.name}!")
        return True

# ---------------- File Handling ----------------
FILE_NAME = "users.json"

def load_users():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except json.JSONDecodeError:
        print(" Warning: users.json file is corrupted. Resetting user data.")
        return []
def save_users(users):
    with open(FILE_NAME, "w") as f:
        json.dump(users, f, indent=4)

def find_user(email):
    users = load_users()
    for user in users:
        if user['email'] == email:
            return user
    return None

# ---------------- Auth Functions ----------------
def signup():
    print("\n SIGN UP")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Create a password: ")
    device = input("Enter your device name: ")

    if find_user(email):
        print(" User already exists. Try logging in.")
        return

    user = Google(name, email, password, device)
    users = load_users()
    users.append(user.to_dict())
    save_users(users)
    print(" Signup successful!")

def login():
    print("\n LOGIN")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    device = input("Detected device: ")

    user_data = find_user(email)
    if not user_data:
        print(" No user found with this email. Try signing up.")
        return

    user = Google(user_data['name'], user_data['email'], user_data['password'], user_data['device'])

    try:
        user.login(email, password, device)
    except (LoginError, SecurityError):
        pass

# ---------------- Menu Interface ----------------
def main():
    while True:
        print("\n========= GOOGLE AUTH =========")
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            signup()
        elif choice == '2':
            login()
        elif choice == '3':
            print(" Disconnected. Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.")

# ---------------- Entry Point ----------------
if __name__ == "__main__":
    main()
