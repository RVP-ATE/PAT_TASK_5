import re

# Function to validate email address
def validate_email(email):
    # Regular expression for email validation
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, email):
        return True
    return False

# Function to validate mobile number of Bangladesh
def validate_bangladesh_mobile(mobile):
    # Regular expression for Bangladesh mobile number (starting with +880 or 01)
    bangladesh_mobile_regex = r'^\+8801[3-9]\d{8}$|^01[3-9]\d{8}$'
    if re.match(bangladesh_mobile_regex, mobile):
        return True
    return False

# Function to validate USA telephone number
def validate_usa_telephone(telephone):
    # Regular expression for USA telephone number (XXX-XXX-XXXX or (XXX) XXX-XXXX)
    usa_telephone_regex = r'^\(\d{3}\)\s\d{3}-\d{4}$|^\d{3}-\d{3}-\d{4}$'
    if re.match(usa_telephone_regex, telephone):
        return True
    return False

# Function to validate 16-character alphanumeric password with special characters
def validate_password(password):
    # Regular expression for a valid password (16 characters, including upper/lowercase, numbers, and special characters)
    password_regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{16}$'
    if re.match(password_regex, password):
        return True
    return False

# Example usage:

# Validate Email Address
email = "test@example.com"
print(f"Email '{email}' valid: {validate_email(email)}")

# Validate Mobile Number of Bangladesh
mobile = "+8801712345678"
print(f"Mobile Number '{mobile}' valid: {validate_bangladesh_mobile(mobile)}")

# Validate USA Telephone Number
telephone = "(123) 456-7890"
print(f"USA Telephone '{telephone}' valid: {validate_usa_telephone(telephone)}")

# Validate Password
password = "Passw0rd@2024!!"
print(f"Password '{password}' valid: {validate_password(password)}")