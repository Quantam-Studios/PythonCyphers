# A1Z26 Cypher

symbols = "!@#$%^&*()_+=<>,.?/:;{}[]| "
alpha = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567891011121314151617181920212223242526"

# methods
def cypher(text):
  cypheredText = ''
  place = 0
  for l in text:
    if l in symbols:
      cypheredText += l
      place += 1
    elif l in alpha:
      letterVal = alpha.find(l) + 1
      cypheredText += str(letterVal)
      if len(text) > place + 1:
        if text[place + 1] in alpha:
          cypheredText += "-" 
      place += 1
  print(cypheredText)

def decypher(text):
  plainText = ''   
  for l in text:
    if l in symbols:
      plainText += l
    elif l in numbers:
      letterVal = alpha[int(l) - 1]
      plainText += str(letterVal)
  print(plainText)
      
# run time
while True:
  answer = input("Type 'c' to cypher plain text\nType 'd' to decypher cyphered text\n")
  if answer == 'c':
    text = input("Type the plain text: ")
    cypher(text)
  if answer == 'd':
    text = input("Type what you would like decyphered: ")
    decypher(text)