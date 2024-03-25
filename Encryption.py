def main():
    method = input ("please enter encrypt or decrypt  ") 
    alphabet = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    if method in [ "Encrypt" , "encrypt"]:
        
     def encrypt(bEncrypt):
        Nencrypt = ""
        for char in bEncrypt:
            if char in alphabet:
                nposition = (alphabet.find(char) + 3) % 26
                Nencrypt += alphabet[nposition]
            else:
                Nencrypt += char
        return Nencrypt
            
     bEncrypt = input ("Enter message to encrypt ")
     bEncrypt = bEncrypt.upper()
     print(encrypt(bEncrypt))
     main()


    elif method in ["Decrypt" , "decrypt"]:
     def decrypt(bDecrypt):
        Ndecrypt = ""
        for char in bDecrypt:
            if char in alphabet:
                nposition = (alphabet.find(char) - 3) % 26
                Ndecrypt += alphabet[nposition]
            else:
              Ndecrypt += char
        return Ndecrypt
            
     bDecrypt = input ("please enter message to decrypt ")
     bDecrypt = bDecrypt.upper()
     print(decrypt(bDecrypt))
     main()
     
    else:
        print("please enter vaild choice")
        main()


main()
