O programa usa Python3

O programa utiliza o método simplex para calcular um valor 
máximo. Para calcular valores mínimos basta lembrar que:
	min z = max -z
e a resposta será dada em um valor positivo, porém se estiver 
calculando o mínimo, deve-se colocar manualmente o sinal 
negativo.
--------------------------------------------------------------------------------
Modelo de entrada

número de linhas:    m
número de colunas: n
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
Usando isso, executará o programa simplex_code.py
###############################################
Caso contrário, há o arquivo simplex.py com o mesmo código.

$ python3 simplex.py
---------------------------------------------------------------------------------