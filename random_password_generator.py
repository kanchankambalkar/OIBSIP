import random
import string

# Ask the user for password length
length = int(input("Enter password length: "))

# Characters to use
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display password
print("Your generated password is:", password)