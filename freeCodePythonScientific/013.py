# O primeiro tipo de cifra que você construirá é chamado de cifra de César. Especificamente, você pegará cada letra da sua mensagem, encontrará sua posição no alfabeto, pegará a letra localizada após 3 posições no alfabeto e substituirá a letra original pela nova letra.
# Para implementar isso, você usará o método .find() discutido na etapa anterior. Modifique sua chamada .find() existente, passando-a text[0] como argumento em vez de 'z'.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet.find(text[0])