#Write a program that encrypts and decrypts strings

def encrypt(string , key):
  return key.join(string)

def decrypt(string , key):
  return string.split(key)

mainString = input("Enter main string : ")
key = input("Enter the encryption key : ")

encryptedString = encrypt(mainString, key)
decryptedLst = decrypt(encryptedString, key)

decryptedString = "".join(decryptedLst)
print("The encrypted string is " , encryptedString)
print("The string after decryption is : " , decryptedString)


