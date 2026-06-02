"""
Simple encryption program for texts.
"""
import random
import string

def main():
    """ Main function to run the encryption program"""
    text: str = input("Enter the text to encrypt: ")
    
    chars = " " + string.ascii_letters + string.digits + string.punctuation
    chars = list(chars)
    keys = chars.copy()
    random.shuffle(keys)
    
    # Encryption
    cipher_text = ""
    
    for letter in text:
        index = chars.index(letter)
        cipher_text += keys[index]
        
    print(f"Encrypted Text: {cipher_text}")

    # Decryption
    decrypted_text = ""
    for letter in cipher_text:
        index = keys.index(letter)
        decrypted_text += chars[index]
    
    print(f"Decrypted Text: {decrypted_text}")
    
if __name__ == "__main__":
    main()