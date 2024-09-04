import secrets
import string


def generate_password(size, include_numbers, include_special):  
    characters = string.ascii_letters
    
    if include_numbers and include_special:
        characters += string.digits + string.punctuation
    
    elif include_numbers:
        characters += string.digits
    
    elif include_special:
        characters += string.punctuation
    
    else:
        characters = string.ascii_letters
    
    return ''.join(secrets.choice(characters) for _ in range(size))
