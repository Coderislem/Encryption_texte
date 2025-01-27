import math
import random

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(min_value, max_value):
    """Generate a random prime number within the given range."""
    prime = random.randrange(min_value, max_value)
    while not is_prime(prime):
        prime = random.randrange(min_value, max_value)
    return prime

def mod_inverse(e, phi):
    """Calculate the modular multiplicative inverse."""
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return (x % phi + phi) % phi

def generate_keypair(bits=8):
    """Generate public and private keypairs."""
    # Generate two random prime numbers
    p = generate_prime(2**(bits-1), 2**bits)
    q = generate_prime(2**(bits-1), 2**bits)
    while p == q:
        q = generate_prime(2**(bits-1), 2**bits)

    n = p * q  # Calculate n
    phi = (p - 1) * (q - 1)  # Calculate phi (Euler's totient function)

    # Choose public exponent e
    e = 65537  # Commonly used value for e
    while math.gcd(e, phi) != 1:
        e += 2

    # Calculate private exponent d
    d = mod_inverse(e, phi)

    return ((e, n), (d, n))  # Return public and private key pairs

def encrypt(public_key, plaintext):
    """Encrypt a message using the public key."""
    e, n = public_key
    # Convert each character to its ASCII value and encrypt
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    """Decrypt a message using the private key."""
    d, n = private_key
    # Decrypt each number and convert back to character
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

def main():
    """Example usage of RSA encryption."""
    # Generate key pairs
    print("Generating RSA keys...")
    public_key, private_key = generate_keypair()
    print(f"Public key: {public_key}")
    print(f"Private key: {private_key}")

    # Test message
    message = "Hello, RSA!"
    print(f"\nOriginal message: {message}")

    # Encrypt the message
    encrypted_msg = encrypt(public_key, message)
    print(f"Encrypted message: {encrypted_msg}")

    # Decrypt the message
    decrypted_msg = decrypt(private_key, encrypted_msg)
    print(f"Decrypted message: {decrypted_msg}")

if __name__ == "__main__":
    main()