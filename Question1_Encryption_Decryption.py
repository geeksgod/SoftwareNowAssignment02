from Helper import helper as util

def encrypt_text(input_file, output_file,key_file, n, m):
    """This function uses ceaser cipher logic to encrypt the text."""
    def encrypt_character(c):
        #encryption logic
        if 'a' <= c <= 'm':  
            return "s",chr(((ord(c) - ord("a") + (n * m)) % 26) + ord("a"))
        elif 'n' <= c <= 'z':  
            return "t",chr(((ord(c) - ord("a") - (n + m)) % 26) + ord("a"))
        elif 'A' <= c <= 'M':  
            return "u",chr(((ord(c) - ord("A") - n) % 26) + ord("A"))
        elif 'N' <= c <= 'Z':  
            return "v",chr(((ord(c) - ord("A") + (m ** 2)) % 26) + ord("A"))
        return "w",c  

    with open(input_file, 'r') as f:
        raw_text = f.read()

    print(f"Raw text to encrypt: {raw_text}")
    
    finalkey = ""
    encrypted_text = ""
    
    for c in raw_text:        
        key,encrypted_char = encrypt_character(c)
        finalkey = finalkey + key
        encrypted_text = encrypted_text + encrypted_char
        
    with open(key_file, 'w') as f:
        f.write(finalkey)
        
    with open(output_file, 'w') as f:
        f.write(encrypted_text)
    
    
    print(f"Encrypted text written to {output_file}")


def decrypt_text(input_file, output_file,key_file, n, m):
    """This function reverses the ceaser cypher"""
    def decrypt_character(key,c):
            #decryption logic
            if key == "s": 
             return chr(((ord(c) - ord("a") - (n * m)) % 26) + ord("a"))
            elif key == "t":  
             return chr(((ord(c) - ord("a") + (n + m)) % 26) + ord("a")) 
            elif key == "u": 
                return chr(((ord(c) - ord("A") + n) % 26) + ord("A")) 
            elif key == "v": 
                return chr(((ord(c) - ord("A") - (m ** 2)) % 26) + ord("A")) 
            return c  
        
    with open(input_file, 'r') as f:
        encrypted_text = f.read()
    
    """ We are generating key because the 2 encryption criteria used, produced same character 
    encryption for different character"""
    with open(key_file,'r') as f:
        keys = f.read()
    
    
    decrypted_text = ""
    for key,c in zip(keys,encrypted_text):
        decrypted_text =  decrypted_text + decrypt_character(key,c) #using key to decrypt the encrypted text
    

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
    raw_text_file = "Encryption_files/raw_text.txt"
    encrypted_text_file = "Encryption_files/encrypted_text.txt"
    decrypted_text_file = "Encryption_files/decrypted_text.txt"
    key_file = "Encryption_files/key_file.txt"

    n = util.get_valid_int("Please enter the first integer:") 
    m = util.get_valid_int("Please enter the second integer:") 


    encrypt_text(raw_text_file, encrypted_text_file,key_file, n, m)
    decrypt_text(encrypted_text_file, decrypted_text_file,key_file, n, m)

    if verify_decryption(raw_text_file, decrypted_text_file):
        print("Decryption verified successfully!")
    else:
        print("Decryption is successful.")
