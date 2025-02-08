#escreva um programa que pergunte o valor total da conta em seguida pergunte quantos clientes existem , divida a conta pelo os clientes e exiba o qaunto cada cliente deve pagar seguida da mensagem "cada cliente deve pagar: x valor"

conta = int (input("Qual o valor total da conta? ")) 
pessoa = int(input("Quantas clientes em questão)"))
print("Cada cliente deve pagar: ",conta/pessoa,"R$")