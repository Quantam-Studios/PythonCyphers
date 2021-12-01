#Atbash cypher

alpha = 'abcdefghijklmnopqrstuvwxyz'
symbols = ":;./?!@#$5&*()+=-_^{}|[] "

# cypher
def cypher(text):
  cypherText = ''
  for l in text:
    if l in symbols:
      cypherText += l
    if l.isalpha():
      # calculate opposite letter value
      finalVal = 25 - alpha.find(l)
      cypherText += alpha[finalVal]
  print(cypherText)

# decypher
def decypher(text):
  plainText = ''
  for l in text:
    if l in symbols:
      plainText += l
    if l.isalpha():
      #calculate the correct letter value
      finalVal =  25 - alpha.find(l)
      plainText += alpha[finalVal]
  print(plainText)

# run time stuff
while True:
  answer = input("Type 'c' is you want to cypher text: \nType 'd' if you want to decypher: \n")
  if answer == 'c':
    text = input("Type the plain text to cypher: ")
    cypher(text)
  if answer == 'd':
    text = input("Type the cyphered text: ")
    decypher(text)