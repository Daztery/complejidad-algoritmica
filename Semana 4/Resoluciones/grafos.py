def LeeMA2MA(filename):
    """
    Funcion lee un archivo que contiene un grafo en formato de matriz de adyacencia
    y retorna una matriz de adyacencia
    """
    file = open(filename)
    i = -1
    for line in file:
        if i == -1:
            n = int(line)
            G = [None for _ in range(n)]
        else:
            G[i] = [int(x) for x in line.split(' ')]
        i +=1
        
    return G

def LeeLA2LA(filename):
    """
    Funcion lee un archivo que contiene un grafo en formato de lista de adyacencia
    y retorna una lista de adyacencia
    """
    G = []
    file = open(filename)
    for line in file:
        G.append([int(x) for x in line.split(' ')])
        
    return G

def str2pair(x):
    """
    Recibe una cadena como '4,5' y retorna una tupla (4, 5)
    """
    nums = x.split(',')
    return int(nums[0]), int(nums[1])

def LeeLAP2LAP(filename):
    """
    Funcion lee un archivo que contiene un grafo en formato de lista de adyacencia
    con pesos y retorna una lista de adyacencia con pesos
    """
    G = []
    file = open(filename)
    for line in file:
        G.append([str2pair(x) for x in line.split(' ')])
        
    return G
