# Coded by: Alex Fox
# Date: September 2021
# Description: Generate random password using python

# Needed Imports
import string
import random
from random import randint

# Parameters for password, uses random integer to select number of each requirement.
# Combined number of requirements will not be greater than 8.
while True:

    num_caps = randint(1, 3)
    num_spc = randint(1, 2)
    num_digits = randint(1, 3)
    pas_req = num_caps + num_spc + num_digits
    pass_len = int(input('How long would you like your password? A minimum of 10 characters is required:'))

    if pass_len >= int(10):
        break
    else:
        print('Your password must be at least 10 characters long. Please try again')

# Random selection for password complexities.
caps = []
for i in range(0, num_caps):
    caps.append(random.choice(string.ascii_letters).upper())

special = []
for i in range(0, num_spc):
    special.append(random.choice(string.punctuation))

digits = []
for i in range(0, num_digits):
    digits.append(random.choice(string.digits))

# Variable to hold the combined random outputs for each requirement.
password_requirements = caps + special + digits

# Taking the current password requirement characters and subtracting them from the password length.
# Making the variable password and generating random lower chase characters that equal password length.
pass_len: int = pass_len - pas_req
password = []
for i in range(0, pass_len):
    password.append(random.choice(string.ascii_letters).lower())

# combining password requirements variable and adding them to the password variable.
for char in password_requirements:
    password.append(char)

# Shuffle all characters in password to help randomize the pattern.
random.shuffle(password)

# Converting variable password into a string.
password = str(password)

# Formatting the password to remove commas, quotes, brackets and white space.
password = password.replace(",", "").replace("'", "").replace("[", "").replace("]", "").replace(" ", "")

# print the password
print(password)
