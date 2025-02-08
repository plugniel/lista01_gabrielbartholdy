#escreva um programa que pergunte o nome do aniversariante, em seguida pergunte a sua idade e acresente mais 1 e exiba o nome do aniversariante seguida da mensagem "no proximo aniversario voca tera" idade mais anos
nome = input("qual seu nome? ")
idade = int (input("qual sua idade? "))
if idade < 0: 
    print("idade invalida")
else:
    print(nome,"no proximo aniversario você tera",idade + 1 ,"anos")