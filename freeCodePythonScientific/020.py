# Como você pode ver na saída, 'h' está no índice 7 na sequência do alfabeto. Agora você precisa encontrar a letra no índice 7 mais o valor de shift. Para isso, você pode usar o operador de adição, +, da mesma forma que usaria para uma adição matemática.
# Modifique sua variável deslocada para que ela armazene o valor do alfabeto no índice índice + deslocamento.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
print(index)
shifted = alphabet[index + shift]
print(shifted)