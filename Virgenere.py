def prepare_text(text):
    """
    Prepare the text by removing spaces and converting to uppercase.
    Returns only alphabetic characters.
    """
    return ''.join(c.upper() for c in text if c.isalpha())

def extend_key(key, length):
    """
    Extend the key to match the length of the text by repeating it.
    """
    key = prepare_text(key)
    return (key * (length // len(key) + 1))[:length]

def vigenere_encrypt(plaintext, key):
    """
    Encrypt text using Vigenère cipher.
    
    Args:
        plaintext (str): The text to encrypt
        key (str): The encryption key
        
    Returns:
        str: The encrypted text
    """
    plaintext = prepare_text(plaintext)
    extended_key = extend_key(key, len(plaintext))
    ciphertext = []
    
    for p, k in zip(plaintext, extended_key):
        # Convert letters to numbers (A=0, B=1, etc.)
        p_num = ord(p) - ord('A')
        k_num = ord(k) - ord('A')
        
        # Apply Vigenère formula: (P + K) mod 26
        c_num = (p_num + k_num) % 26
        
        # Convert back to letter
        ciphertext.append(chr(c_num + ord('A')))
    
    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, key):
    """
    Decrypt text using Vigenère cipher.
    
    Args:
        ciphertext (str): The text to decrypt
        key (str): The decryption key
        
    Returns:
        str: The decrypted text
    """
    ciphertext = prepare_text(ciphertext)
    extended_key = extend_key(key, len(ciphertext))
    plaintext = []
    
    for c, k in zip(ciphertext, extended_key):
        # Convert letters to numbers (A=0, B=1, etc.)
        c_num = ord(c) - ord('A')
        k_num = ord(k) - ord('A')
        
        # Apply Vigenère formula: (C - K) mod 26
        p_num = (c_num - k_num) % 26
        
        # Convert back to letter
        plaintext.append(chr(p_num + ord('A')))
    
    return ''.join(plaintext)

def print_vigenere_table():
    """
    Print the Vigenère table (tabula recta).
    """
    print("\nVigenère Table (Tabula Recta):")
    print("  " + " ".join([chr(i + ord('A')) for i in range(26)]))
    print("  " + "-" * 51)
    
    for i in range(26):
        row = chr(i + ord('A')) + "|"
        for j in range(26):
            row += " " + chr(((i + j) % 26) + ord('A'))
        print(row)

def main():
    """
    Example usage of the Vigenère cipher.
    """
    # Print the Vigenère table
    print_vigenere_table()
    
    # Example encryption
    plaintext = "HELLO WORLD"
    key = "KEY"
    
    print(f"\nPlaintext: {plaintext}")
    print(f"Key: {key}")
    
    # Encrypt
    encrypted = vigenere_encrypt(plaintext, key)
    print(f"Encrypted: {encrypted}")
    
    # Decrypt
    decrypted = vigenere_decrypt(encrypted, key)
    print(f"Decrypted: {decrypted}")
    
    # Show the encryption process
    print("\nEncryption Process:")
    plaintext = prepare_text(plaintext)
    extended_key = extend_key(key, len(plaintext))
    print(f"Prepared text: {plaintext}")
    print(f"Extended key:  {extended_key}")
    print(f"Result:       {encrypted}")

if __name__ == "__main__":
    main()