# **Desenvolvimento das funcionalidade em falta no código do jogo Minibingo**

ficheiro minibingo.py

# **Análise de Código**

## **Bloco 1**
No bloco de código em questão, poderia ser usado um único ciclo "for" contendo as três operações "if", dado que os três ciclos em questão correspondem a três iteração iguais.

## **Bloco 2**
A necessidade da conversão do valor `params[21]` em int na terceira linha sugere que o valor não corresponda a um int, logo a operação `params[21] - 3`, realizada na primeira linha, pode provocar um erro. Na hipótese de `params[21]` se tratar efetivamente de uma valor int, a sua conversão na terceira linha seria desnecessária.

## **Bloco 3**
Relativamente ao método `take` representado no bloco 3, considera-se que a verificação do número de elementos do iterable e o respetivo lançamento da exceção deverá ser feito anteriormente ao ciclo "while", de forma a que este não seja executado em consequência do lançamento da exceção.

## **Bloco 4**
Dado que o método `base64url_decode` se destina à descodificação de dados em formato string ou bytes, é necessário assegurar o tratamento de dados que não correspondam a um destes dois tipos, através de uma condição que verifique o seu tipo e eventualmente através do lançamento de uma exceção adequada em caso negativo.

## **Bloco 5**
Relativamente ao bloco 5, considerando que foi criado o objecto `error`, é desnecessária a instanciação de um segundo a partir do "raise", bastando adicionar a mensagem personalizada do erro à exceção no `logger`, como se pode ver no seguinte bloco:

    try:
    	do_some_stuff()
    except Exception as error:
    	logger.exception("an error has occurred: {}".format(error))
    	raise error 

## **Bloco 6**
Dado que as operações realizadas em todas as condições "if" são iguais exceto para `x == 'C'` na operação `step2`, só é necessária a introdução da condição neste último caso, conforme se pode ver no seguinte bloco:

    step1(x + x)
    step2(x + 'A') if x=='C' else step2(x + x)
    stepN(x + x)

## **Bloco 7**
Pressupondo que o lançamento da exceção "TypeError" ocorre dentro da função `check_type`, o método `parse` implementado no bloco 7 encontra-se corretamente implementado, cobrindo os 4 resultados possíveis (`val` não corresponder a uma "string", `val` corresponder a uma valor "True", "False" e `val` não ser reconhecido segundo o conjunto de valores booleanos estipulados).


## **Bloco 8**
O bloco de código 8 corresponde ao cabeçalho de uma função com 10 parâmetros diferentes. Em circunstâncias normais, a utilização de um elevado número de parâmetros constitui uma má prática, contradizendo o princípio de encapsulamento de OOP dado que retira flexibilidade ao código.

## **Bloco 9**
Relativamente à linha de código representada no bloco 9, o valor atribuído à variável `bonus_finish` poderia ser feito de forma mais simples/intuitiva:

    bonus_finish = kwargs["bonus_finish"] == "1"
