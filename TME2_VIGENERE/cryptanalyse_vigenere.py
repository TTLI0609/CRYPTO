#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Sorbonne Universite 3I024 2018-2019
# TME 2 : Cryptanalyse du chiffre de Vigenere
#
# Etudiant.e 1 : BERRICHI Ilham 3522116
# Etudiant.e 2 : LY Tingting 3679785

import sys, getopt, string, math

# Alphabet francais
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Frequence moyenne des lettres en francais
# a modifier
freq_FR = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


def frequence(file):
	"""
	file = ficher sur lequel on va appliquer la fonction 
	return liste contenant fréquence d'apparition de chaque lettre 
	de l'alphabet dans le fichier "file" passé en argument de la fonction
	"""
	f = open(file, "r")
	text = f.read()
	
	cpt=0
	list =[]
	for i in range(len(alphabet)):
		list.append( (text.count(alphabet[i]) *1.0 ) / len(text))
	
	f.close()
	return list

freq_FR = frequence("germinal.txt")
#print(freq_FR)


def rotation (x):
	"""
	x = int qui indique de combien on veut décaler la premiere
		 lettre de l'alphabet
	return le nouvel alphabet obtenu avec le décalage souhaité
	"""
	return alphabet[x:] + alphabet[:x]

#test
#print(rotation(3))

def index (l):
	"""
	l = lettre de l'alphabet
	return l'indice de cette lettre dans l'alphabet
	"""
	for i in range(len(alphabet)) :
		if l == alphabet[i]:
			return i
	return -1

#test
#print(index("E"))



def chiffre_cesar(txt, key):
	"""
	txt = le message clair
	key = la clef
	return le message chiffrÃ©
	"""
	new_alpha = rotation(key)
	res = ""
	
	for i in txt:
		res += new_alpha[index(i)]
	
	txt = res
	return txt

#print(chiffre_cesar("BONJOUR",3))


# Dechiffrement Cesar
def dechiffre_cesar(txt, key):
	"""
	txt = le message chiffre
	key = la clef
	return le message clair
	
	"""
	if(key == 0):
		vrai_alpha = alphabet
	else: 
		vrai_alpha = rotation(index(alphabet[26-key]) )
	res = ""
	
	for i in txt:
		res += vrai_alpha[index(i)]
	
	txt = res
	return txt



# Chiffrement Vigenere
def chiffre_vigenere(txt, key):
	"""
	txt = le message clair
	key = la clef
	return le message chiffre
	"""
	i =0
	res = ""
	for j in txt:
		res += alphabet[(index(j)+key[i%len(key)] ) %26]
		i += 1
	return res

#print(chiffre_vigenere("ALICE", [0]))


# Dechiffrement Vigenere
def dechiffre_vigenere(txt, key):
	"""
	txt = le message chiffrÃ©
	key = la clef
	return le message clair
	
	"""
	i =0
	res = ""
	for j in txt:
		res += alphabet[((index(j)-key[i%len(key)] )+26) %26]
		i += 1
	return res

#print(dechiffre_vigenere("ALICE", [0]))


# Analyse de frequences
def freq(txt):
    """
    txt = texte à etudier
    return une liste contenant les frequences d'apparition 
    dans le texte de chaque lettre de l'alphabet 
    """
    list =[]
    for i in range(len(alphabet)):
        list.append( (txt.count(alphabet[i]) *1.0) ) 
        

    return list



def lettre_freq_max(txt):
	"""
	txt = texte à etudier
	return l'indice dans l'alphabet de la lettre la plus frÃ©quente d'un texte
	"""
	list = freq(txt)
	max = list[0]
	imax = 0
	for i in range(1,len(list)):
		if max < list[i]:
			max = list[i]
			imax = i
	return imax



# indice de coincidence
def indice_coincidence(hist):
	"""
	hist = tableau contenant les frequences des lettres d'un texte
	return indice de coincidence
	"""
	res = 0
	som = sum(hist)
	for i in range(0,len(hist)):
		res += ((hist[i] / som) * ((hist[i]-1) / (som -1)))
	return res
    

# Recherche la longueur de la clef
def longueur_clef(cipher):
	"""
	cipher = texte
	return la taille de la clé
	"""
	list=[]
	IC = []
	for i in range (1, 21):
		for j in range(0,i):
			list = cipher[j::i]
			f = freq(list)
			IC.append(indice_coincidence(f))
		
		moy = sum(IC)/len(IC)
		IC.clear()
		if moy > 0.06:
			return i
    

# Renvoie le tableau des decalages probables etant
# donner la longueur de la clef
# en utilisant la lettre la plus frequente
# de chaque colonne
def clef_par_decalages(cipher, key_length):
	"""
	cipher = texte à déchiffrer
	key_length = taille de la clé
	return tableau de décalage permettant le déchiffrement du texte
	"""
	decalages=[0]*key_length
	for i in range (0, key_length):
		list = cipher[i::key_length]
		a = lettre_freq_max(list)
		clef = ((22 - (26 - a))  +26) %26   #22 correspond a 26-index('E')
		decalages[i] = clef
	return decalages

#print(clef_par_decalages("GHGHGH",2))



# Cryptanalyse V1 avec décalages par frequence max
def cryptanalyse_v1(cipher):
	"""
	cipher = texte à cryptanalyser
	return le message déchiffré
	"""
	key_length = longueur_clef(cipher)
	listc = clef_par_decalages(cipher, key_length)
	res=""
	j = 0
	for i in cipher:
		res += dechiffre_cesar(i, listc[j % key_length] )
		j +=1
	return res


#print(cryptanalyse_v1("GHGHGH"))


"""
 Combien de textes sont correctement cryptanalysés ? 
	=> 18 textes sont correctement cryptanalysés.
 
 Comment expliquez-vous cela ?
	=> Sur des textes courts par exemple, l'indice de coincidence peut être erroné ainsi 
	la longueur de la clef trouvé sera aussi fausse.
	Il faut donc un texte assez long.
"""

################################################################


### Les fonctions suivantes sont utiles uniquement
### pour la cryptanalyse V2.

# Indice de coincidence mutuelle avec décalage
def indice_coincidence_mutuelle(h1,h2,d):
	"""
	h1 = Tableau de frequences des lettres du texte 1
	h2 = Tableau de frequences des lettres du texte 2
	return l'indice de coincidence mutuelle avec decalage
	"""
	
	res = 0.0
	tot = sum(h1) * sum(h2)
	h2 = h2[d:] + h2[:d]
	for i in range (0,26):
		res += (h1[i]*h2[i]) / tot
	return res




# Renvoie le tableau des décalages probables étant
# donné la longueur de la clé
# en comparant l'indice de décalage mutuel par rapport
# à la première colonne
def tableau_decalages_ICM(cipher, key_length):
	"""
	cipher = texte 
	key_length = longueur de la cle
	return tableau des décalages probables
	"""
	decalages=[0]*key_length
	colonne1 = cipher[0::key_length]
	dec = clef_par_decalages(cipher, key_length)
	
	for i in range (1, key_length):
		colonnei = cipher[i::key_length]
		
		max=0.0
		maxj = 0
		for j in range(0, 26):
			tmp  = indice_coincidence_mutuelle(freq(colonne1),freq(colonnei),j)
			if max < tmp:
				max = tmp
				maxj = j
		decalages[i] = maxj
	print(decalages)
	return decalages



# Cryptanalyse V2 avec décalages par ICM
def cryptanalyse_v2(cipher):
	"""
	cipher = texte à cryptanalyser avec decalage par ICM
	return le texte déchiffré
	"""
	key_length = longueur_clef(cipher)
	listc = tableau_decalages_ICM(cipher, key_length)
	res=""
	j = 0
	for i in cipher:
		res += dechiffre_cesar(i, listc[j % key_length] )
		j +=1
		
	f= freq(res)
	max=f[0]
	ind=0
	for i in range(len(f)):
		if (max<f[i]) :
			max= f[i]
			ind = i
			
	rot = ind - index('E') 
	
	res = dechiffre_cesar(res, index(alphabet[rot]))
	return res

"""
Combien de textes sont correctement cryptanalysés ? 
	=> 43 textes sont correctement cryptanaysés
	
Comment expliquez-vous cela ? 
	=>

"""

################################################################


### Les fonctions suivantes sont utiles uniquement
### pour la cryptanalyse V3.

# Prend deux listes de même taille et
# calcule la correlation lineaire de Pearson
def correlation(L1,L2):
    """
    L1 = liste de même taille que L2 et qui correspond à une variable
    L2 = liste de même taille que L1 et qui correspond à une variable
    return la correlation entre ces 2 listes
    """
    esperanceL1 = sum(L1) / len(L1)
    esperanceL2 = sum(L2) / len(L2)
    
    res =0.0
    resX= 0.0
    resY =0.0
    
    for i in range(len(L1) ):
        resX += (L1[i]- esperanceL1)**2
        resY += (L2[i]- esperanceL2)**2
        res += (L1[i]- esperanceL1) * (L2[i]- esperanceL2)
    resX = math.sqrt(resX*resY)
    return res / resX

# Renvoie la meilleur clé possible par correlation
# étant donné une longueur de clé fixée
def clef_correlations(cipher, key_length):
    """
    Documentation à écrire
    """
    key=[0]*key_length
    score = 0.0
    maxTmp = -2
    jmax=0
    for i in range (0, key_length):
        colonnei = cipher[i::key_length]
        freqCol = freq(colonnei)
        freqColTmp = freqCol
        
        for j in range(0,26):
            freqColTmp = freqCol[j:] + freqCol[:j]
            
            tmp = correlation(freqColTmp,freq_FR)
            if(tmp > maxTmp ):
                maxTmp = tmp
                jmax=j
                
        key[i]=jmax
        score += maxTmp
        maxTmp = -2
        
    print(key)

    score= score/ key_length
    print(score)
    return (score, key)

# Cryptanalyse V3 avec correlations
def cryptanalyse_v3(cipher):
    """
    Documentation à écrire
    """
    score = 0
    key=[]
    for i in range(1,21):
        (scoreTmp, keyTmp) = clef_correlations(cipher, i)
        if(score < scoreTmp):
            score = scoreTmp
            key = keyTmp

    return dechiffre_vigenere(cipher, key)

"""
Combien de textes sont correctement cryptanalysés ? 
    => 94 textes correctement cryptanalysés
Quels sont les caractéristiques destextes qui échouent ? 
    =>

Comment expliquez-vous cela ?


"""


################################################################
# NE PAS MODIFIER LES FONCTIONS SUIVANTES
# ELLES SONT UTILES POUR LES TEST D'EVALUATION
################################################################


# Lit un fichier et renvoie la chaine de caracteres
def read(fichier):
    f=open(fichier,"r")
    txt=(f.readlines())[0].rstrip('\n')
    f.close()
    return txt

# Execute la fonction cryptanalyse_vN où N est la version
def cryptanalyse(fichier, version):
    cipher = read(fichier)
    if version == 1:
        return cryptanalyse_v1(cipher)
    elif version == 2:
        return cryptanalyse_v2(cipher)
    elif version == 3:
        return cryptanalyse_v3(cipher)

def usage():
    print ("Usage: python3 cryptanalyse_vigenere.py -v <1,2,3> -f <FichierACryptanalyser>", file=sys.stderr)
    sys.exit(1)

def main(argv):
    size = -1
    version = 0
    fichier = ''
    try:
        opts, args = getopt.getopt(argv,"hv:f:")
    except getopt.GetoptError:
        usage()
    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt in ("-v"):
            version = int(arg)
        elif opt in ("-f"):
            fichier = arg
    if fichier=='':
        usage()
    if not(version==1 or version==2 or version==3):
        usage()

    print("Cryptanalyse version "+str(version)+" du fichier "+fichier+" :")
    print(cryptanalyse(fichier, version))
    
if __name__ == "__main__":
   main(sys.argv[1:])
