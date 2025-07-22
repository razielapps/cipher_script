#version 2 of the cipher script, more user friendly and usable also improved with a user interface

alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

img = """
//   ▗▄▄▗▄▄▄▗▄▄▖▗▖ ▗▗▄▄▄▗▄▄▖  ▗▄▄▖ ▗▄▄▗▄▄▖▗▄▄▄▗▄▄ ▗▄▄▄▖
//  ▐▌    █ ▐▌ ▐▐▌ ▐▐▌  ▐▌ ▐  ▐▌  ▐▌  ▐▌ ▐▌ █ ▐▌ ▐▌ █  
//  ▐▌    █ ▐▛▀▘▐▛▀▜▐▛▀▀▐▛▀▚▖  ▝▀▚▐▌  ▐▛▀▚▖ █ ▐▛▀▘  █  
//  ▝▚▄▄▗▄█▄▐▌  ▐▌ ▐▐▙▄▄▐▌ ▐  ▗▄▄▞▝▚▄▄▐▌ ▐▗▄█▄▐▌    █  
//                                                  
//                                                  
//                                                  
"""
print(img)
print("Welcome to Cipher Script")
def ceasar():
    while True:
        print("What would you like to do? 1. Encode 2. Decode 0. Exit\n ")
        try:
            choice = int(input(">>> "))
        except:
            print("Please select a valid option")
            break
        match choice:
            case 1:
                 #encode
                 print("Encoding...")
                 print("Please enter a message to encode\n")
                 text_to_encode = input(">>> ")
                 print("How many shift? \n")
                 shift = int(input(">>> "))
                 cipher_text = ""
                 for letter in text_to_encode:
                    position = alphabet.index(letter)
                    new_position = position + shift
                    new_letter = alphabet[new_position]
                    cipher_text += new_letter
                 print("The endcoded text is ",cipher_text+"\n")
            
            case 2:
                #decode

                 print("Decoding...")
                 print("Please enter a message to decode\n")
                 text_to_decode = input(">>> ")
                 print("How many shifts?\n")
                 shift = int(input(">>> "))
                 plain_text = ""
                 for letter in text_to_decode:
                    position = alphabet.index(letter)
                    new_position = position - shift
                    plain_text += alphabet[new_position]
                 print("The decoded message is",plain_text +"\n")
            case 0:
                print("Thank you for using Cipher Script")
                break
            case __:
                print("The system does not understand your inout. Shutting down....")

ceasar()
