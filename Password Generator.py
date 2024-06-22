import secrets
import string

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    selection_list = letters + digits + special_chars
    password = ''.join(secrets.choice(selection_list) for _ in range(length))
    return password

password_length = int(input("Enter the desired length of the password: "))
password = generate_password(password_length)
print("Generated Password is :",password)
