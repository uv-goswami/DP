import hashlib
import requests

def check_password_pwned(password):
    """
    Checks if a password has been leaked using Have I Been Pwned's API.
    Returns the number of times it was found in breaches (0 if not found).
    """
    # Hash the password using SHA-1
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    
    # First 5 characters for K-anonymity
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]
    
    # Query the API
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching data: {response.status_code}")
    
    # Check if suffix is in the returned list
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)  # Number of times found
    
    return 0  # Not found


def check_passwords_from_file(filename):
    """
    Reads a file with 'username,password' per line and checks each password.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            username, password = line.strip().split(',')
            count = check_password_pwned(password)
            if count:
                print(f"⚠️ Password for user '{username}' has been leaked {count} times.")
            else:
                print(f"✅ Password for user '{username}' is safe (not found in breaches).")


# Example usage
if __name__ == "__main__":
    file_path = "passwords.txt"  # Example file
    check_passwords_from_file(file_path)