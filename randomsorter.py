import random as ran
while True:
	x = int(input("Insira o numero de pessoas: "))
	i = 0
	lista =[]
	while(i!= x):
		value = ran.randrange(x+1)
		if value in lista:
			continue
		if value == 0 :
			continue
		lista.append(value)
		i = i+1
	posi = ran.randrange(x)
	print(lista[posi])


