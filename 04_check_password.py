import hashlib
import requests

def check_password_leak(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return 0
            
        hashes = (line.split(':') for line in response.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                return int(count)
        return 0
    except:
        return 0

filename = "credentials.txt"
try:
    with open(filename, "w") as f:
        f.write("admin,password123\n")
        f.write("user,SuperSecureP@ss\n")
        f.write("test,123456\n")
except:
    pass

try:
    with open(filename, "r") as file:
        print(f"{'USERNAME':<15} | {'PASSWORD':<20} | {'STATUS'}")
        print("-" * 55)
        
        for line in file:
            parts = line.strip().split(',')
            if len(parts) >= 2:
                user = parts[0]
                pwd = parts[1]
                
                count = check_password_leak(pwd)
                
                if count > 0:
                    print(f"{user:<15} | {pwd:<20} | LEAKED ({count} times)")
                else:
                    print(f"{user:<15} | {pwd:<20} | SAFE")
except FileNotFoundError:
    print("File not found.")
