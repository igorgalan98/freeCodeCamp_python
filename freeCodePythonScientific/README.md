Exercícios de "Computação científica com Python" do site freeCodeCamp



000 - Criando uma variável


001 - As variáveis ​​podem armazenar valores de diferentes tipos de dados. Você acabou de atribuir um valor inteiro, mas se quiser representar alguma texto, será necessário atribuir uma string. Strings são sequências de caracteres entre aspas simples ou duplas, mas você não pode iniciar uma string com aspas simples e terminá-la com aspas duplas ou vice-versa.


002 - Você pode usar a função integrada print() para imprimir a saída do seu código no terminal. Funções são blocos de código reutilizáveis ​​que você pode chamar ou invocar para executar seu código quando precisar deles. Para chamar uma função, basta escrever um par de parênteses ao lado de seu nome. Você aprenderá mais sobre funções em breve.


003 - Um argumento é um objeto ou uma expressão passada para uma função — adicionada entre os parênteses de abertura e fechamento — quando ela é chamada.


004 - Cada caractere de string pode ser referenciado por um índice numérico. A contagem do índice começa em zero. Portanto, o primeiro caractere de uma string tem um índice 0. Por exemplo, na string 'Hello World', 'H' está no índice 0, 'e' está no índice 1 e assim por diante. Cada caractere de uma string pode ser acessado usando a notação de colchetes. Você precisa escrever o nome da variável seguido de colchetes e adicionar o índice do caractere entre colchetes.


005 - Você também pode acessar caracteres de string começando no final da string. O último caractere tem um índice de -1, o penúltimo -2 e assim por diante. Agora modifique sua chamada print() existente para imprimir o último caractere da sua string.


006 - Você pode acessar o número de caracteres em uma string com a função len() integrada. Modifique sua chamada print() existente passando len(text) em vez de text[-1].


007 - Outra função integrada útil é type(), que retorna o tipo de dados de uma variável. Modifique sua chamada print() para imprimir o tipo de dados do texto.


008 - Como você pode ver, a saída de print type(text) é class 'str', o que significa que sua variável é uma string, indicada como str. Agora vá para uma nova linha e crie outra variável chamada shift e atribua o valor 3 a esta variável.
 

009 - Use print para a nova variável


010 - Modifique sua chamada print(shift) para imprimir o tipo de dados de sua variável shift.


011 - Algumas palavras são palavras-chave reservadas (por exemplo, para, enquanto, Verdadeiro). Eles têm um significado especial em Python, portanto você não pode usá-los para nomes de variáveis. Variable names cannot start with a number, and they can only contain alpha-numeric characters or underscores. Os nomes das variáveis ​​diferenciam maiúsculas de minúsculas, ou seja, my_var é diferente de my_Var e MY_VAR. Finalmente, é uma convenção comum escrever nomes de variáveis ​​usando Snake_case, onde cada espaço é substituído por um caractere de sublinhado e as palavras são escritas em letras minúsculas. Remova ambas as chamadas para print() e declare outra variável chamada alfabeto. Atribua a string 'abcdefghijklmnopqrstuvwxyz' a esta variável.


012 - Você usará o método .find() para encontrar a posição no alfabeto de cada letra da sua mensagem. Um método é semelhante a uma função, mas pertence a um objeto.


013 - O primeiro tipo de cifra que você construirá é chamado de cifra de César. Especificamente, você pegará cada letra da sua mensagem, encontrará sua posição no alfabeto, pegará a letra localizada após 3 posições no alfabeto e substituirá a letra original pela nova letra. Para implementar isso, você usará o método .find() discutido na etapa anterior. Modifique sua chamada .find() existente, passando-a text[0] como argumento em vez de 'z'.


014 - A função print() fornece apenas uma saída no console, mas funções e métodos podem ter um valor de retorno que você pode usar em seu código. Agora atribua alpha.find(text[0]) a uma variável chamada index. Desta forma, o índice armazenará o valor retornado por alfabeto.find(text[0]).


015 - A seguir, imprima a variável de índice no console.


016 - .find() retorna o índice do caractere correspondente dentro da string. Se o caractere não for encontrado, retorna -1. Como você pode ver, o primeiro caractere do texto, 'H' maiúsculo, não foi encontrado, pois o alfabeto contém apenas letras minúsculas. Você pode transformar uma string em seu equivalente em minúsculas com o método .lower(). Adicione outra chamada print() para print text.lower() e veja a saída.


017 - Remova a última chamada print(). Então, em vez de text[0], passe text[0].lower() como argumento para sua chamada .find() e veja a saída.


018 - Declare uma nova variável chamada shifted. Use a notação de colchetes para acessar o valor do alfabeto no índice e atribuí-lo à sua nova variável.


019 - Imprima sua variável shifted.


020 - Como você pode ver na saída, 'h' está no índice 7 na sequência do alfabeto. Agora você precisa encontrar a letra no índice 7 mais o valor de shift. Para isso, você pode usar o operador de adição, +, da mesma forma que usaria para uma adição matemática. Modifique sua variável deslocada para que ela armazene o valor do alfabeto no índice índice + deslocamento.


021 - Repetir o processo de localização da letra dentro do alfabeto e determinar a letra deslocada para cada caractere do texto pode ser entediante. Felizmente, você pode simplificá-lo usando um loop. Por enquanto, remova todas as linhas de código abaixo da declaração da variável alfabeto.



022 - 
023 - 
024 - 
025 - 
026 - 
027 - 
028 - 
029 - 
030 - 
031 - 
032 - 
033 - 
034 - 
035 - 
036 -
037 -
038 -
039 -
040 - 
041 -
042 -
043 - 
044 -
045 -
046 -
047 -
048 -
049 -
050 -
051 -
052 -
053 -
054 -
055 -
056 -
057 -
058 -
059 -
060 -
061 -
062 -
063 -
064 -
065 -
066 -
067 -
068 -
069 -
070 -
071 -
072 -
073 -
074 -
075 -
076 -
077 -
078 -
079 -
080 -
081 -
082 -
083 -
084 -
085 -
086 -
087 -
088 -
089 -
090 -
091 -
092 -
093 -
094 -
095 -
096 -
