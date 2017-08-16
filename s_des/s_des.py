P10 = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
P8 = (6, 3, 7, 4, 8, 5, 10, 9)
P4 = (2, 4, 3, 1)

IP = (2, 6, 3, 1, 4, 8, 5, 7)
InversedIP = (4, 1, 3, 5, 7, 2, 8, 6)
EP = (4, 1, 2, 3, 2, 3, 4, 1)

S0 = 	([1, 0, 3, 2],
		[3, 2, 1, 0],
		[0, 2, 1, 3],
		[3, 1, 3, 2])

S1 = 	([0, 1, 2, 3],
		[2, 0, 1, 3],
		[3, 0, 1, 0],
		[2, 1, 0, 3])

def permutate(key, pattern):
    newKey = ''
    for each in pattern:
        newKey += key[each - 1]

    return newKey

def getLeft(key):
    return key[:int(len(key)/2)]

def getRight(key):
    return key[int(len(key)/2):]

def shift(key):
    return key[1:] + key[0]

def key1(key):
	key1 = permutate(key, P10)
	key1 = shift( getLeft(key1) ) + shift( getRight(key1) )
	key1 = permutate(key1, P8)
	return key1

def key2(key):
	key2 = permutate(key, P10)
	for i in range(0,3):
		key2 = shift( getLeft(key2) ) + shift( getRight(key2) )
	key2 = permutate(key2, P8)
	return key2

def encrypt(text):
	text = permutate(text, IP)

def decrypt(text):
	pass
