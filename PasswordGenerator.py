import random
import string

def generate_password(length=12):
    #Define the possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    #Ensure the password has at least one of each type of character
    password = [
        random.choice(string.ascii_uppercase),  # at least one uppercase letter
        random.choice(string.ascii_lowercase),  # at least one lowercase letter
        random.choice(string.digits),           # at least one digit
        random.choice(string.punctuation)       # at least one special character
    ]
    
    #Fill the rest of the password length with random characters
    password += random.choices(characters, k=length - 4)
    
    #Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    #Convert the list to a string and return
    return ''.join(password)

# Example usage
password_length = 12
password = generate_password(password_length)
print(f"Generated password: {password}")
