# Vigenere cypher

alpha = "abcdefghijklmnopqrstuvwxyz"
symbols = ":;./?!@#$5&*()+=-_^{}|[] "

#cypher
def cypher(text, key):
  # create Cyphered Text
  cypherText = ''
  x = 0
  for l in text:
    if l in symbols:
      cypherText += l
    if l.isalpha():
      # calculate the letter value of the cyphered letter
      finalLetterVal = alpha.find(key[x]) + alpha.find(l)
      # add the new letter to cypherText
      if finalLetterVal < 26:
        cypherText += alpha[finalLetterVal]
      elif finalLetterVal >= 26:
        finalLetterVal -= 26
        cypherText += alpha[finalLetterVal]
      # cycle through key
      x += 1
      if x == len(key):
        x = 0
  # print cypherText
  print(cypherText)


#decypher
def decypher(cypherText, key):
  # create plain text
  plainText = ''
  x = 0
  for l in cyText:
    if l in symbols:
      plainText += l
    if l.isalpha():
      #calculate the letter value of the unshifted letter
      finalVal = alpha.find(l) - alpha.find(key[x])
      # add the new letter to the plain text
      if finalVal >= 0:
        plainText += alpha[finalVal]
      elif finalVal < 0:
        finalVal += 26
        plainText += alpha[finalVal]
      # cycle through key
      x += 1
      if x == len(key):
        x = 0
  print(plainText)

while True:
  choice = input("Type 'c' to cypher something \nType 'd' to decypher something \n")
  if choice == 'c':
    text = input("Type the plain text you want cyphered: ")
    key = input("Type the key: ")
    cypher(text, key)
  if choice == 'd':
    cyText = input("Type the cyphered text: ")
    key = input("Type the key: ")
    decypher(cyText, key)