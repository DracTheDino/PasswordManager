import haslib
import json

# Run for the first time. 

with open('.passwords.json') as f:
    passwords = json.load(f)

print("Welcome to Drac's PasswordManager. ")
print("You will be setting up your master password right now. ")

print("\nPlease enter your new master password. Be sure to remember it. ")
new_master_password = input(">")

passwords["master"] = hashlib.sha256(new_master_passwords.encode())

print("Great, we'll set this up quickly. ")

with open(".passwords.json", "w") as outfile:
    json.dump(passwords, outfile)
