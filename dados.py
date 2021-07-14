from random import randint

def main():
	nd = obter_numero_de_dados()
	
	nl = definir_numero_de_lados(nd)
	
	for i in nl:
		n = randint(1, i)
		print(n)
	

def obter_numero_de_dados():
	# Obter inputs do usuário
	while True:
		n = input("Número de dados: ")
		
		# Verificar se n é um dígito
		if not n.isdigit():
			continue
		
		# Transformar n em inteiro
		n = int(n)
		
		# Verificar se o usuário digitou o número certo
		if n < 1:
			continue
		return n


def definir_numero_de_lados(n):
	if n == 1:
		while True:
			# Obter número de lados
			l = input("Quantos lados? [min. 6] ")
			
			# Verificar se l é um dígito
			if not l.isdigit():
				continue
	
			# Transformar l em inteiro
			l = int(l)
			
			# Verificar se o usuário digitou o número certo
			if l < 6:
				continue
			return [l]
	while True:
		# Verificar se os dados têm o mesmo número de lados
		q = input("Os dados tem o mesmo número de lados? [s/n] ")
		q = q.lower()
		lados_de_cada_dado = []
		
		if q == "s":
			while True:
				# Obter número de lados
				l = input("Quantos? [min. 6] ")
				
				# Verificar se l é um dígito
				if not l.isdigit():
					continue
		
				# Transformar l em inteiro
				l = int(l)
				
				# Verificar se o usuário digitou o número certo
				if l < 6:
					continue

				lados_de_cada_dado.append(l)
				return lados_de_cada_dado
		elif q == "n":
			for i in range(n):
				while True:
					# Obter número de lados
					aux = str(i + 1)
					l = input("Quantos lados tem o dado " + aux + "? [min. 6] ")
					# Verificar se l é um dígito
					if not l.isdigit():
						continue
			
					# Transformar l em inteiro
					l = int(l)
					
					if l < 6:
						continue
					break
				lados_de_cada_dado.append(l)
			return lados_de_cada_dado



if __name__ == "__main__":
	main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
