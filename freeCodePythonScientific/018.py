# Declare uma nova variável chamada shifted. Use a notação de colchetes para acessar o valor do alfabeto no índice e atribuí-lo à sua nova variável.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
shifted = alphabet[index]
print(index)