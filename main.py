from ceaser_logo import *

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

replay = True

while replay == True:  

    print(" ")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n\n")
    print(" ")
    text = input("Type your message:\n\n").lower()
    print(" ")
    shift = int(input("Type the shift number:\n\n"))

    def ceaser(t, s, d):   
        encripted_word = ""
        for letter in text:
            if letter in alphabet:
                index_num = alphabet.index(letter)
                if d == "encode":
                    encripted_word += alphabet[(index_num + shift) % 26]
                else:
                    encripted_word += alphabet[(index_num - shift)]
            else:
                encripted_word += letter
        
        print(" ")
        print(encripted_word)
        

    ceaser(text, shift, direction)

    print(" ")
    question_answer = input("Would you like to replay? Y or N:\n\n")
    if question_answer == "N":
        replay = False