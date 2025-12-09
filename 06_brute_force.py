import itertools
import string
import time

def simulate_brute_force(target_password):
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    start_time = time.time()
    
    for length in range(1, 9):
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess_word = "".join(guess)
            
            if guess_word == target_password:
                end_time = time.time()
                return guess_word, attempts, end_time - start_time
                
    return None, attempts, 0

target = input("Enter a weak password (max 4 chars for speed): ")
print(f"Cracking '{target}'...")

cracked_password, count, duration = simulate_brute_force(target)

if cracked_password:
    print(f"Success! Password is: {cracked_password}")
    print(f"Total Attempts: {count}")
    print(f"Time Taken: {duration:.5f} seconds")
else:
    print("Failed to crack within limit.")
