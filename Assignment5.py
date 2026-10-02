sentence = input("Enter the coded message: ")
secret = input("Enter the secret message: ")

if secret.lower() in sentence.lower():
    print("Secret message found!")
else:
    print("Secret message not found.")