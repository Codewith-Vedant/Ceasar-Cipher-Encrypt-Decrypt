def caesar_cipher(text, shift, mode='encrypt'):
    if mode == 'decrypt':
        shift = -shift

    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

def main():
    print("Caesar Cipher Program")
    while True:
        choice = input("Do you want to encrypt or decrypt a message? (e/d): ").lower()
        if choice in ['e', 'd']:
            break
        else:
            print("Invalid choice, please enter 'e' for encryption or 'd' for decryption.")
    
    message = input("Enter the message: ")
    while True:
        try:
            shift = int(input("Enter the shift value (integer): "))
            break
        except ValueError:
            print("Invalid shift value, please enter an integer.")
    
    if choice == 'e':
        result = caesar_cipher(message, shift, mode='encrypt')
        print(f"Encrypted message: {result}")
    else:
        result = caesar_cipher(message, shift, mode='decrypt')
        print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
