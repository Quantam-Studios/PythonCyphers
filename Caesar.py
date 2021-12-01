# cipher, and decipher strings

# initial variables
symbols = "!#$?,. "
plainText = ''
shift = ''

# cipher function (encrypt)
def cipher(plainText, shift): 
    cipherText = ""
    for ch in plainText:
        if ch.isalpha():
            remainInAlpha = ord(ch) + shift 
            if remainInAlpha > ord('z'):
                remainInAlpha -= 26
            finalLetter = chr(remainInAlpha)
        elif ch in symbols:
          finalLetter = ch
        cipherText += finalLetter

    print ("Your ciphered text is: ", cipherText)

    return cipherText

# decipher function (decrypt)
def decipher(cipherText): 
    x = 0
    shiftTest = 1
    solutions = []
    while x < 25:
      decipheredText = ""
      for ch in cipherText:        
        if ch.isalpha():
            remainInAlpha = ord(ch) + shiftTest
            if remainInAlpha > ord('z'):
                remainInAlpha -= 26
            finalLetter = chr(remainInAlpha)
        elif ch in symbols:
          finalLetter = ch
        decipheredText += finalLetter
      solutions.append(decipheredText + " \n Shift of: " + str(26 - shiftTest))
      x += 1
      shiftTest += 1
    print("List of solutions: ")
    for s in solutions:
      print ("\n", s)
    return decipheredText
    
# Main Loop
while True:
  answer = input("Type 'd' to decipher a string" + "\n" + "Type 'c' to cipher a string " + "\n" + "c or d: ")
  if answer == "c":
    plainText = input("What is your message? ")
    shift = int(input("What is your shift? "))
    cipher(plainText, shift)

  if answer == "d":
    cipheredText = input("What is your ciphered message?: \n")
    decipher(cipheredText)
  
