import random
import string

print("Welcome to the Strong Password Generator!")

# Ask the user how long they want the password
length = int(input("Enter password length (e.g., 8, 12, 16): "))

# Define possible characters
letters = string.ascii_letters
numbers = string.digits
symbols = "!@#$%^&*()?"

# Combine all characters
all_characters = letters + numbers + symbols

# Generate random password
password = ''.join(random.choice(all_characters) for i in range(length))

print("Your generated password is:", password)
