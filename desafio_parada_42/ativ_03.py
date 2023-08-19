import os

codigo = input("Digite o código do produto: ")
nome = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade do produto: "))
preco = float(input("Digite o preço do produto: "))

total = (preco*quantidade)

print(" Código:",codigo," \n Nome:",nome," \n Quantidade:",quantidade," \n Preço:",preco," \n O valor total da compra é",total)

os.system("pause")