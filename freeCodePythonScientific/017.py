# Remova a última chamada print(). Então, em vez de text[0], passe text[0].lower() como argumento para sua chamada .find() e veja a saída.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
print(index)