def encrypt_text(input_file, output_file, n, m):
    print("Starting encryption...")
    def encrypt_character(c):
        if 'a' <= c <= 'm':  
            return chr(((ord(c) - ord('a') + (n * m)) % 26) + ord('a'))
        elif 'n' <= c <= 'z':  
            return chr(((ord(c) - ord('a') - (n + m)) % 26) + ord('a'))
        elif 'A' <= c <= 'M':  
            return chr(((ord(c) - ord('A') - n) % 26) + ord('A'))
        elif 'N' <= c <= 'Z':  
            return chr(((ord(c) - ord('A') + (m ** 2)) % 26) + ord('A'))
        return c  

    with open(input_file, 'r') as f:
        raw_text = f.read()

    print(f"Raw text to encrypt: {raw_text}")
    encrypted_text = ''.join(encrypt_character(c) for c in raw_text)

    with open(output_file, 'w') as f:
        f.write(encrypted_text)
    print(f"Encrypted text written to {output_file}")


def decrypt_text(input_file, output_file, n, m):
    print("Starting decryption...")
    def decrypt_character(c):
            if 'a' <= c <= 'm': 
             return chr(((ord(c) - ord('a') - (n * m)) % 26) + ord('a'))
            elif 'n' <= c <= 'z':  
             return chr(((ord(c) - ord('a') - (n + m)) % 26) + ord('a')) 
            elif 'A' <= c <= 'M': 
                return chr(((ord(c) - ord('A') - n) % 26) + ord('A')) 
            elif 'N' <= c <= 'Z': 
                return chr(((ord(c) - ord('A') - (m ** 2)) % 26) + ord('A')) 
            return c  
    with open(input_file, 'r') as f:
        encrypted_text = f.read()

    print(f"Encrypted text to decrypt: {encrypted_text}")
    decrypted_text = ''.join(decrypt_character(c) for c in encrypted_text)

    with open(output_file, 'w') as f:
        f.write(decrypted_text)
    print(f"Decrypted text written to {output_file}")


def verify_decryption(original_file, decrypted_file):
    print("Verifying decryption...")
    with open(original_file, 'r') as f:
        original_text = f.read()

    with open(decrypted_file, 'r') as f:
        decrypted_text = f.read()

    print(f"Original text: {original_text}")
    print(f"Decrypted text: {decrypted_text}")
    return original_text == decrypted_text


if __name__ == "__main__":
    print("Program started...")
    raw_text_file = "Encryptionfiles/raw_text.txt"
    encrypted_text_file = "Encryptionfiles/encrypted_text.txt"
    decrypted_text_file = "Encryptionfiles/decrypted_text.txt"

    n = 2  
    m = 3 
    with open(raw_text_file, 'w') as f:
        f.write("Hello, this is a test file!@#@$@JHKHJKH123123")

    encrypt_text(raw_text_file, encrypted_text_file, n, m)
    decrypt_text(encrypted_text_file, decrypted_text_file, n, m)

    if verify_decryption(raw_text_file, decrypted_text_file):
        print("Decryption verified successfully!")
    else:
        print("Decryption is successful.")
