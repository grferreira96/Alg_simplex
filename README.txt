O programa usa Python3

O programa utiliza o m�todo simplex para calcular um valor 
m�ximo. Para calcular valores m�nimos basta lembrar que:
	min z = max -z
e a resposta ser� dada em um valor positivo, por�m se estiver 
calculando o m�nimo, deve-se colocar manualmente o sinal 
negativo.
--------------------------------------------------------------------------------
Modelo de entrada

n�mero de linhas:    m
n�mero de colunas: n
Matriz A:                    x[0][0] ... x[0][n]
		...
		x[m][0] ... x[m][n]
coeficientes b	b[0]
		b[1]
		b[n]
Coeficientes C	C[0]
		C[1]
		C[m]
--------------------------------------------------------------------------------
Como compilar?

$ chmod +777 simplex.sh
$ ./simplex
Usando isso, executar� o programa simplex_code.py
###############################################
Caso contr�rio, h� o arquivo simplex.py com o mesmo c�digo.

$ python3 simplex.py
---------------------------------------------------------------------------------