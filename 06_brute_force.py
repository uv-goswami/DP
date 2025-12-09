import itertools
import string
import time

def brute_force_attack(target_password, max_length=4):
    """
    Simulates a brute-force attack by trying all possible combinations
    of letters, digits, and symbols up to max_length.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    attempts = 0
    start_time = time.time()

    for length in range(1, max_length + 1):
        for guess_tuple in itertools.product(characters, repeat=length):
            attempts += 1
            guess = ''.join(guess_tuple)
            if guess == target_password:
                end_time = time.time()
                print(f"Password found: {guess}")
                print(f"Attempts: {attempts}")
                print(f"Time taken: {end_time - start_time:.2f} seconds")
                return
    print("Password not found within given max_length.")

# Example usage
if __name__ == "__main__":
    password = input("Enter the password to brute-force (for demo, keep it short): ")
    max_len = int(input("Enter maximum length to try: "))
    brute_force_attack(password, max_length=max_len)