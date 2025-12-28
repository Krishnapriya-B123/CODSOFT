# PASSWORD GENERATOR

import random
import string

# Take password length from user
length = int(input("Enter the desired password length: "))

# Define characters to use in password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""
for i in range(length):
    password += random.choice(characters)

# Display the generated password
print("Generated Password:", password)