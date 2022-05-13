## Vernam (one time pad) cipher implementation in Python.

## general variables
alpha = "abcdefghijklmnopqrstuvwxyz"

## cipher
def cipher(plainText, keyText, spaceOrNot):
  pt = plainText
  finalText = ""
  x = 0
  for letter in pt:
    shift = 0
    if letter == " ":
      # increment through the key 
      if x == len(keyText) - 1:
        x = 0;
      else:
        x += 1
      if spaceOrNot == True:
        # add a space if user selected to keep spaces
        finalText += " "
    else:
      # determine the shift 
      # get plainText int
      shift += alpha.find(letter)
      # get keyText int
      shift += alpha.find(keyText[x])
      # ensure shift is not too large
      if shift >= 26:
        shift = shift - 26
        finalText += alpha[shift]
      else:
        finalText += alpha[shift]
      # increment through the key 
      if x == len(keyText) - 1:
        x = 0;
      else:
        x += 1   
  # print the final result
  print(finalText)
  

## decipher
def decipher(cipherText):
  print("Not implemented currently.")
  


## Infinite Loop
while True:
  answer = input("Type 'c' to cipher, type 'd' to decipher: ")
  ## then cipher
  if answer == 'c':
    plainText = input("Type plain text: \n")
    keyText = input("Type the key (must be as long as the previously inserted plain text): \n")
    while len(keyText) != len(plainText):
      print("\nIncorrect length, you need: " + str(len(plainText) - len(keyText)) + " more characters \n")
      keyText = input("Type the key (must be as long as the previously inserted plain text): \n")
    # check if a space is present in the plain text
    spaceOrNot = False;
    if ' ' in plainText:
      # if a spaced is present then prompt user
      spaces = input("Would you like for spaces to stay present, or be taken out of the final cipher?\nType 's' to keep spaces or type 'n' for no spaces: ")
      while spaces != 's' and spaces != 'n':
        spaces = input("Would you like for spaces to stay present, or be taken out of the final cipher?\nType 's' to keep spaces or type 'n' for no spaces: ")
      if spaces == 's':
        spaceOrNot = True
    # create cipher and print when done
    cipher(plainText, keyText, spaceOrNot)
    
  ## decipher
  if answer == "d":
    print("Not implemented yet.\n")
    # -to be added later- cipherText = input("Type ciphered text: \n")
  ## if none then repeat
  
  