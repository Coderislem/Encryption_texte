def prepare_key(key):
    """
    Prepare the key square (5x5 matrix) from the given key.
    Combines I and J into one cell.
    """
    key = key.upper().replace('J', 'I').replace(' ', '')
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Note: I/J are combined
    
    # Remove duplicates from key while maintaining order
    key_chars = []
    for char in key + alphabet:
        if char not in key_chars:
            key_chars.append(char)
    
    # Create the 5x5 matrix
    matrix = []
    for i in range(0, 25, 5):
        matrix.append(key_chars[i:i+5])
    
    return matrix

def find_position(matrix, char):
    """Find the position of a character in the key square."""
    char = 'I' if char == 'J' else char
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

def prepare_text(text):
    """
    Prepare the plaintext/ciphertext:
    - Convert to uppercase
    - Replace J with I
    - Handle repeated letters by inserting 'X'
    - Ensure text length is even by appending 'X' if needed
    """
    text = text.upper().replace('J', 'I').replace(' ', '')
    result = []
    i = 0
    
    while i < len(text):
        if i == len(text) - 1:
            result.extend([text[i], 'X'])
            break
        elif text[i] == text[i + 1]:
            result.extend([text[i], 'X'])
            i += 1
        else:
            result.extend([text[i], text[i + 1]])
            i += 2
            
    return ''.join(result)

def encrypt_pair(matrix, pair):
    """Encrypt a pair of characters according to Playfair rules."""
    row1, col1 = find_position(matrix, pair[0])
    row2, col2 = find_position(matrix, pair[1])
    
    if row1 == row2:  # Same row
        return (matrix[row1][(col1 + 1) % 5], 
                matrix[row2][(col2 + 1) % 5])
    elif col1 == col2:  # Same column
        return (matrix[(row1 + 1) % 5][col1], 
                matrix[(row2 + 1) % 5][col2])
    else:  # Rectangle case
        return (matrix[row1][col2], 
                matrix[row2][col1])

def decrypt_pair(matrix, pair):
    """Decrypt a pair of characters according to Playfair rules."""
    row1, col1 = find_position(matrix, pair[0])
    row2, col2 = find_position(matrix, pair[1])
    
    if row1 == row2:  # Same row
        return (matrix[row1][(col1 - 1) % 5], 
                matrix[row2][(col2 - 1) % 5])
    elif col1 == col2:  # Same column
        return (matrix[(row1 - 1) % 5][col1], 
                matrix[(row2 - 1) % 5][col2])
    else:  # Rectangle case
        return (matrix[row1][col2], 
                matrix[row2][col1])

def playfair(text, key, mode='encrypt'):
    """
    Encrypt or decrypt text using Playfair cipher.
    mode: 'encrypt' or 'decrypt'
    """
    # Prepare the key matrix
    matrix = prepare_key(key)
    
    # Prepare the text
    prepared_text = prepare_text(text)
    
    # Process pairs
    result = []
    for i in range(0, len(prepared_text), 2):
        pair = prepared_text[i:i+2]
        if mode == 'encrypt':
            new_pair = encrypt_pair(matrix, pair)
        else:
            new_pair = decrypt_pair(matrix, pair)
        result.extend(new_pair)
    
    return ''.join(result)

def print_matrix(matrix):
    """Print the key square matrix in a readable format."""
    print("\nKey Square Matrix:")
    print("-----------------")
    for row in matrix:
        print(" ".join(row))
    print("-----------------")

# Example usage
def main():
    key = "PLAYFAIR EXAMPLE"
    plaintext = "HELLO WORLD"
    
    # Show key matrix
    matrix = prepare_key(key)
    print_matrix(matrix)
    
    # Encrypt
    encrypted = playfair(plaintext, key, mode='encrypt')
    print(f"\nPlaintext: {plaintext}")
    print(f"Encrypted: {encrypted}")
    
    # Decrypt
    decrypted = playfair(encrypted, key, mode='decrypt')
    print(f"Decrypted: {decrypted}")

if __name__ == "__main__":
    main()