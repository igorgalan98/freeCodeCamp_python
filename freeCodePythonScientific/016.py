# .find() retorna o índice do caractere correspondente dentro da string. Se o caractere não for encontrado, retorna -1. Como você pode ver, o primeiro caractere do texto, 'H' maiúsculo, não foi encontrado, pois o alfabeto contém apenas letras minúsculas.
# Você pode transformar uma string em seu equivalente em minúsculas com o método .lower(). Adicione outra chamada print() para print text.lower() e veja a saída.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0])
print(index)
print(text.lower())