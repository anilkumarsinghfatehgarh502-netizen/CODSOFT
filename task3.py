import random
import string
def generate_password(length):
# Define character sets
    ch = string.ascii_letters + string.digits + string.punctuation
# Generate password 
    password =''.join(random.choice(ch) for _ in range(length))
    return password

# step 1: user input
try:
    length=int(input("Enter the desired password length:"))
    if length <= 0:
        print ("Password length must be greater than 0.")
    else:
        # Step 2: Generate password
        password = generate_password(length)
        # step 3: Display password
        print("Generated password:",password)

except ValueError:
    print("invalid input!Please enter a number.")


