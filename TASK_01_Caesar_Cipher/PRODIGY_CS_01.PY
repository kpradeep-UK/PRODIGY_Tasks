def print_title():
    # ASCII Art Title with Spacing
    title = """
  _____                              _____ _   _ _ _ _  __   __  __  __ _    
 / ____|                            / ____| ||  | | | | | |||||  |        )  
| |     __ _  ___  ___  __ _ _ __  | |    | || |      } | |      |    ) ) )
| |    / _` |/ _ \/ __|/ _` | '__| | |    | || |      } | |||||  |  | |\  ) 
| |___| (_| |  __/\__ \ (_| | |    | |____| || | | | |  | |      |  | \ |  
 \_____\__,_|\___||___/\__,_|_|     \_____|_||_|        |_|||||  |__|  \|  
                              
                                                        
"""
    print(title)


def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

if __name__ == "__main__":
    print_title()
    
    while True:
        print("\nCaesar Cipher Tool")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '3':
            print("Exiting the Caesar Cipher tool. Goodbye!")
            break

        text = input("Enter the text: ")
        shift = int(input("Enter shift value (e.g., 3): "))

        if choice == '1':
            print("Encrypted Text:", caesar_cipher(text, shift, mode='encrypt'))
        elif choice == '2':
            print("Decrypted Text:", caesar_cipher(text, shift, mode='decrypt'))
        else:
            print("Invalid Option. Please choose 1, 2, or 3.")
