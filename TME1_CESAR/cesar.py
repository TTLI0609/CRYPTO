import sys

#######################################
# CONSIGNE
# Modifier uniquement les fonctions suivantes :
# - chiffrer_cesar
# - dechiffrer_cesar
#######################################

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rotation (x):
	x=index(x)
	return alphabet[x:] + alphabet[:x]




#test
#print(rotation(3))


def index (l):
	for i in range(len(alphabet)) :
		if l == alphabet[i]:
			return i
	return -1

#test
#print(index("E"))

	
def chiffrer_cesar(message_clair, clef):
	new_alpha = rotation(clef)
	res = ""
	
	for i in message_clair:
		res += new_alpha[index(i)]
	
	message_chiffre = res
	return message_chiffre


#print(chiffrer_cesar("BONJOUR",3))


def dechiffrer_cesar(message_clair, clef):
	vrai_alpha = rotation(alphabet[26-index(clef)])
	res = ""
	
	for i in message_clair:
		res += vrai_alpha[index(i)]
	
	message_chiffre = res
	return message_chiffre

#print(dechiffrer_cesar("ERQMRXU",3))



# NE PAS MODIFIER APRES CETTE LIGNE
"""
def usage():
    print ("Usage : python cesar.py clef c/d phrase",file=sys.stderr)
    print ("Exemple 1 : python cesar.py E c ALICE",file=sys.stderr)
    print ("\t > EPMGI",file=sys.stderr)
    print ("Exemple 2 : python cesar.py E d EPMGI",file=sys.stderr)
    print ("\t > ALICE",file=sys.stderr)
    sys.exit(1)

if len(sys.argv) != 4:
    usage()
    
clef = sys.argv[1]
operation = sys.argv[2]
phrase = sys.argv[3]

if operation == 'c' : 
    phrase2 = chiffrer_cesar(phrase, clef)
elif operation == 'd' :
    phrase2 = dechiffrer_cesar(phrase, clef)
else:
    usage()
print(phrase2)

"""