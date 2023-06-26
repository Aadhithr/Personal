message = input("Enter a message to encode or decode:")
characterShift = int(input("How many characters do you want to shift the alphabet?:"))
message = message.upper()
output = " "
for letter in message:
    if letter.isupper():
        value = ord(letter) + characterShift
        letter = chr(value)
        if not letter.isupper():
            value -=26
            letter = chr(value)
    output += letter
print("Output message: ", output)
