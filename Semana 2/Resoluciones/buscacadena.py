def ocurrencias(texto, palabra):
	l = len(palabra)
	n = len(texto)
	
	res = []
	
	for i in range(n - l + 1):
		if texto[i] == palabra[0]:
			encontrado = True
			for j in range(1, l):
				if texto[i + j] != palabra[j]:
					encontrado = False
					break
			if encontrado:
				res.append(i)
			
	return res
	
print(ocurrencias("abracadabracalamazoo",
                  "rac"))