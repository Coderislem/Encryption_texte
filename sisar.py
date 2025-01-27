import random

def substitution(text, mode, key=None):
    """
    Function for first and second substitution
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    if mode == "encrypt":
        # If no key is provided, create a new one
        shuffled = ''.join(random.sample(alphabet, len(alphabet)))
        mapping = {k: v for k, v in zip(alphabet, shuffled)}
        return ''.join(mapping.get(char, char) for char in text), shuffled
    elif mode == "decrypt" and key:
        mapping = {v: k for k, v in zip(alphabet, key)}
        return ''.join(mapping.get(char, char) for char in text)

def insertion(text, insert_key):
    """
    Function to insert the key into the text
    """
    interval = 3  # Number of characters before key insertion
    result = []
    key_index = 0
    for i, char in enumerate(text):
        result.append(char)
        if (i + 1) % interval == 0 and key_index < len(insert_key):
            result.append(insert_key[key_index])
            key_index += 1
    return ''.join(result)

def rotation(text, n):
    """
    Function to rotate the text
    """
    n = n % len(text)
    return text[-n:] + text[:-n]

def encrypt_sisar(plaintext, insert_key):
    """
    Complete encryption process
    """
    # 1. First substitution
    substituted_text, subst_key_1 = substitution(plaintext, "encrypt")
    
    # 2. Insertion
    inserted_text = insertion(substituted_text, insert_key)
    
    # 3. Second substitution
    substituted_text_2, subst_key_2 = substitution(inserted_text, "encrypt")
    
    # 4. Rotation
    rotated_text = rotation(substituted_text_2, 5)  # Rotate 5 positions
    
    return rotated_text, subst_key_1, subst_key_2

def decrypt_sisar(ciphertext, insert_key, subst_key_1, subst_key_2):
    """
    Complete decryption process
    """
    # 1. Reverse rotation
    rotated_back_text = rotation(ciphertext, -5)
    
    # 2. Reverse second substitution
    substituted_back_text_2 = substitution(rotated_back_text, "decrypt", subst_key_2)
    
    # 3. Reverse insertion
    removed_text = ''.join([char for i, char in enumerate(substituted_back_text_2) 
                           if (i % 4 != 3)])  # Remove inserted key every 4 positions
    
    # 4. Reverse first substitution
    plaintext = substitution(removed_text, "decrypt", subst_key_1)
    
    return plaintext

# Testing the program
plaintext = "HELLO"
insert_key = "123"

# Encryption
encrypted_text, subst_key_1, subst_key_2 = encrypt_sisar(plaintext, insert_key)
print("Encrypted text:", encrypted_text)
print("First key:", subst_key_1)
print("Second key:", subst_key_2)

# Decryption
decrypted_text = decrypt_sisar(encrypted_text, insert_key, subst_key_1, subst_key_2)
print("Decrypted text:", decrypted_text)