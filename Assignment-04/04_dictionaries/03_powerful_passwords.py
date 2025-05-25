import hashlib


# You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!

# This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier. This is done using a hash function. Luckily, there are several resources that can help us with this.

# For example, using a hash function called SHA256(...) something as simple as

# hello

# can be hashed into a much more complex

# 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

# Fill out the login(...) function for a website that hashes their passwords. Login should return True if an email's stored password hash in stored_logins is the same as the hash of password_to_check.

# (Hint. You will need to use the provided hash_password(...) function. You don't necessarily need to know how it works, just know that hash_password(...) returns the hash for the password!)


def hash_password(password):
    """Hash a password using SHA256"""
    encoded_password = password.encode()
    hash_obj = hashlib.sha256(encoded_password)
    return hash_obj.hexdigest()

def login(email, password_to_check, stored_logins):

    if email not in stored_logins:
        return False
    
    hashed_password = hash_password(password_to_check)
    
    return hashed_password == stored_logins[email]

if __name__ == "__main__":
    stored_logins = {
        "user@example.com": hash_password("securepass123"),
        "admin@example.com": hash_password("adminpass456")
    }
    
    # Test login function
    print(login("user@example.com", "securepass123", stored_logins))  
    print(login("user@example.com", "wrongpassword", stored_logins))  
    print(login("nonexistent@example.com", "anypassword", stored_logins))  