alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


circle=False

while not circle:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(message,direction):
#     word=""
#     for letters in message:
#         position=alphabet.index(letters)
#         new_position=position + direction
#         word+=alphabet[new_position]
#     print(word)

# def decrypt(message,direction):
#     word=""
#     for letters in message:
#         position=alphabet.index(letters)
#         new_position=position - direction
#         word+=alphabet[new_position]
#     print(word)

# if direction == "encode":
#     encrypt(message=text,direction=shift)

# else:
#     decrypt(message=text,direction=shift)

    def caesar(message,length,path):
        word=""
        for letters in message:
            position=alphabet.index(letters)
            if path=="encode":
               new_Position=position + length
               word+=alphabet[new_Position]
                
            if path=="decode":
               new_Position=position -length
               word+=alphabet[new_Position]
        print(f"The result is {word}")

      
    
    caesar(message=text,length=shift,path=direction)           
    entry=input("Do you wish to continue, type 'yes' or 'no':\n")
    if entry=="no":
       circle=True
       print("Thank you for using our medium")
    else:
       circle=False