#!/usr/bin/python3.12

''' Password Complecity Checker'''
import argparse
import re

# Define password criteria
password_policy_criteria = [
    {"criteria": "Minimum Length", "value": 12},
    {"criteria": "Uppercase Letters Required", "value": True},
    {"criteria": "Lowercase Letters Required", "value": True},
    {"criteria": "Numbers Required", "value": True},
    {"criteria": "Special Characters Required", "value": True},
    {"criteria": "Avoid Common Passwords", "value": True},  # Add list of common passwords if needed
]

# Function to check password criteria
def check_password_strength(password):
    feedback = []

    # Check length
    if len(password) < password_policy_criteria[0]['value']:
        feedback.append(f"Password should be at least {password_policy_criteria[0]['value']} characters long.")

    # Check uppercase letters
    if password_policy_criteria[1]['value'] and not any(c.isupper() for c in password):
        feedback.append("Password must include at least one uppercase letter.")

    # Check lowercase letters
    if password_policy_criteria[2]['value'] and not any(c.islower() for c in password):
        feedback.append("Password must include at least one lowercase letter.")

    # Check numbers
    if password_policy_criteria[3]['value'] and not any(c.isdigit() for c in password):
        feedback.append("Password must include at least one number.")

    # Check special characters
    special_characters = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    if password_policy_criteria[4]['value'] and not special_characters.search(password):
        feedback.append("Password must include at least one special character.")

    # Check against common passwords (optional)
    common_passwords = ["password123", "123456", "qwerty", "admin123", "iloveyou",]  # Add more if needed
    if password_policy_criteria[5]['value'] and password.lower() in common_passwords:
        feedback.append("Password is too common. Choose a more unique password.")

    if not feedback:
        feedback.append("Password is strong.")
    
    return feedback


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Password Complecity Checker ",
    usage="python PRODIGY_CS_03.py password@123 ")
    
    parser.add_argument("password",type=str,help="Enter Password")
    args = parser.parse_args()

feedback = check_password_strength(args.password)
for line in feedback:
    print(line)
