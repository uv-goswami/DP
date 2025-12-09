import random

def generate_password_from_dict(dict_file, num_words=4, separator='-'):
    """
    Generates a password by randomly selecting words from a dictionary file.
    """
    with open(dict_file, 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file if line.strip()]
    
    if len(words) < num_words:
        raise ValueError("Dictionary file does not have enough words.")
    
    chosen_words = random.sample(words, num_words)
    return separator.join(chosen_words)


if __name__ == "__main__":
    dict_path = "05dictionary.txt"  # Path to your dictionary file
    num = int(input("Enter number of words for password: "))
    sep = input("Enter separator (default '-'): ") or '-'
    
    password = generate_password_from_dict(dict_path, num_words=num, separator=sep)
    print(f"Generated Password: {password}")