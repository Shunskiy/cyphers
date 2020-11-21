import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
def encrypt(m,k):
    k *= len(m) // len(k) + 1
    c = ''.join([chr((ord(j) + ord(k[i])) % 26 + ord('A')) for i, j in enumerate(m)])
    print(c)
    
def decrypt(c,k):
    k *= len(c) // len(k) + 1
    m = ''.join([chr((ord(j) - ord(k[i])) % 26 + ord('A')) for i, j in enumerate(c)])
    print(m)
    
def main():
    reserv = 1
    while reserv:
        print("Encrypt, Decrypt, eXit(e/d/x): ")
        check = input()
        if check == "e":
            print("Encrypt word: ")
            encrypt_word = input()
            encrypt_word = encrypt_word.upper()
            print("Key: ")
            key = input()
            key = key.upper()
            encrypt(encrypt_word, key)
        elif check == "d":
            print("Decrypt word: ")
            decrypt_word = input()
            decrypt_word = decrypt_word.upper()
            print("key: ")
            key = input()
            key = key.upper()
            decrypt(decrypt_word, key)
        elif check == "x":
            reserv = 0
        else:
            cls()
            
main()
    