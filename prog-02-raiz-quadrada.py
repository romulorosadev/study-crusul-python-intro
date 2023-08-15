# PROBLEMA:
# Apresentar a raiz quadrada de um número digitado pelo usuário

# MEU RACIONAL 
# 1) Importar a bibliteca math para poder utilizar as funções disponibilizadas
# 2) Solicitar o valor via teclado e armazenar numa variável já no tipo float
# 3) Uso da função math.sqrt pra calcular a raiz quadrda do numero passado como parâmetro. Atribuir o valor a uma variavel
# 4) Exibir no terminal o valor informado pelo usuário
# 5) Exibir no terminal o valor do calculo da raiz quadrada do número informado


#1
import math

#2
inNumero = float(input("Informe um número pra calcularmos sua raiz quadrada: "))

#3
outResultado = math.sqrt(inNumero)

#4
print("Número Informado:", inNumero)

#5
print("Raiz Quadrada do Número Informado:", outResultado)