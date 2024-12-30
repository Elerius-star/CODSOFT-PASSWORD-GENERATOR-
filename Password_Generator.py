import random
import string

# Step 1: Display a welcome message
print("Welcome to the Password Generator!")

# Step 2: Prompt the user for password length
try:
    length = int(input("Enter the desired password length (minimum 8): "))
    if length < 8:
        print("Password length must be at least 8 for complexity.")
        exit()
except ValueError:
    print("Please enter a valid number.")
    exit()

# Step 3: Ask for complexity preferences
print("Include the following in your password:")
include_uppercase = input("Uppercase letters? (y/n): ").lower() == 'y'
include_lowercase = input("Lowercase letters? (y/n): ").lower() == 'y'
include_numbers = input("Numbers? (y/n): ").lower() == 'y'
include_specials = input("Special characters? (y/n): ").lower() == 'y'

# Step 4: Build the character set
character_pool = ""
if include_uppercase:
    character_pool += string.ascii_uppercase
if include_lowercase:
    character_pool += string.ascii_lowercase
if include_numbers:
    character_pool += string.digits
if include_specials:
    character_pool += string.punctuation

if not character_pool:
    print("You must select at least one character type.")
    exit()

# Step 5: Generate the password
password = ''.join(random.choices(character_pool, k=length))

# Step 6: Display the password
print(f"Your generated password is: {password}")

