

decrescente = True
anterior = int(input("Digite o primeiro numero da sequencia: "))
valor = 1
while valor != 0 and decrescente:
		valor = int(input(" digete um numero da sequrncia: "))
		if valor > anterior:
			descrecente = false
		anterior  = valor

if decrescente:
		print("a seguencia esta em ordem decrescente")
else:
		print("a sequencia nao esta em ordem decrescente")