import sys

#######################################
# CONSIGNE
# Modifier uniquement les fonctions suivantes :
# - chiffrer_mono
# - dechiffrer_mono
#######################################

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def index (l):
	for i in range(len(alphabet)) :
		if l == alphabet[i]:
			return i
	return -1

def index_dechi (l,alpha):
	for i in range(len(alpha)) :
		if l == alpha[i]:
			return i
	return -1


def chiffrer_mono(message_clair, clef):
    # MODIFIER LE CODE ICI
    res=[]
    
    for i in message_clair:
        ind = index(i)
        res += clef[ind]
        
    message_chiffre = res
    return message_chiffre

#print(chiffrer_mono("ALICE","QWERTYUIOPASDFGHJKLZXCVBNM"))


def dechiffrer_mono(message_clair, clef):
    res=[]
    
    for i in message_clair:
        ind = index_dechi(i,clef)
        res += alphabet[ind]
        
    message_chiffre = res
    return message_chiffre

#print(dechiffrer_mono("QSOET","QWERTYUIOPASDFGHJKLZXCVBNM"))


# NE PAS MODIFIER APRES CETTE LIGNE

def usage():
    print ("Usage : python mono.py clef c/d phrase",file=sys.stderr)
    print ("Exemple 1 : python mono.py QWERTYUIOPASDFGHJKLZXCVBNM c ALICE",file=sys.stderr)
    print ("\t > QSOET",file=sys.stderr)
    print ("Exemple 2 : python mono.py QWERTYUIOPASDFGHJKLZXCVBNM d QSOET",file=sys.stderr)
    print ("\t > ALICE",file=sys.stderr)
    sys.exit(1)

if len(sys.argv) != 4:
    usage()
    
clef = sys.argv[1]
operation = sys.argv[2]
phrase = sys.argv[3]

if operation == 'c' : 
    phrase2 = chiffrer_mono(phrase, clef)
elif operation == 'd' :
    phrase2 = dechiffrer_mono(phrase, clef)
else:
    usage()
print(phrase2)
