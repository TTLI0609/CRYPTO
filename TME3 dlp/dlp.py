from prime import is_probable_prime
import math 
import random


#Exercice 1
#Q1
def pgcd(a, b):
    """
    :param a: entier positif
    :param b: entier positif
    :return: pgcd de a et b
    """
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

#print(pgcd(90,123))      #3


def bezout(a, b):
    """
    :param a: entier positif
    :param b: entier positif
    :return: le pgcd et les deux coefficients de Bezout de a et b
    """

    r0 = a
    r1 = b 
    u0 = 0
    u1 = 1 - u0
    v0 = 1
    v1 = int(-r0/r1 )               # 0 - (int(-r0/r1 )*1)
    
    res = [r1, u0, v0]              # pgcd, u, v
    while r0%r1 :                   #tant que le prochain reste qu'on va trouver est different de 0 
        r = r0                      #r = r(i-1)
        r0 = r1     
        r1 = r%r1                   #r1 = reste de r(i-1)/r(i)
        u = u0     
        v = v0 
        u0 = u1 
        v0 = v1 
        q = int(r0/r1)             #partie entiere
        u1 = u-q*u1 
        v1 = v-q*v1 
        
        res = [r1,u0,v0] 
    return res

#rint(bezout(789,360))

#Q2
def inv_mod(a, n):
    """
    :param a: entier positif
    :param n: groupe Z/nZ
    :return: l'inverse de a dans Z/nZ s'il existe
            sinon retourne False
    """

    (r, u, v ) = bezout(a, n)
    if r == 1:                  #si pgcd = 1 alors inversible 
        return u % n
    else :
        #print(a,"n'est pas inversible dans Z/",n,"Z.")
        return False

#print(inv_mod(5,7))

def invertibles(N):
    """
    :param N: groupe Z/NZ
    :return: la liste des elements inversibles dans Z/NZ
    """
    res = list()
    for i in range(N):
        if(inv_mod(i,N) != False):
            res.append(i)
    return res 

#print(invertibles(12))

#Q3
def phi(N):
    """
    :param N: entier positif
    :return: le nombre d'entier inferieur a N et premier avec N
    """
    res = 0
    for i in range(N):
        if pgcd(i,N) == 1:
            res += 1
    return res

#print(phi(12))


#Exercice 2
#Q1

def exp(a, n, p):
    """
    :param a: entier positif
    :param n: puissance entier positif
    :param p: groupe Z/pZ
    :return: resultat de a^n dans le groupe Z/pZ
    """
    res =1
    while n != 0: 
        if n%2 == 1:    #si n impaire
            res = (res * a)%p
            n = n-1
        else :          #n paire
            a = (a*a)%p
            n = n / 2

    return res

#print(exp(2, 10, 323))

#Q2
def factor(n):
    """
    :param n: enteir positif
    :return: un dictionnaire (facteur premier : valuation p-adique associé)
    """
    fact = []       #recherche de la liste de facteur 1er
    if n==1:
        return fact
    
    while n>=2:  # recherche de tous les facteurs 2 s'il y en a
        x,r = divmod(n,2)
        if r!=0:
            break
        fact.append(2)
        n = x
    
    i=3					# recherche des facteurs 1er >2
    rn = sqrt(n)+1
    while i<=n:
        if i>rn:
            fact.append(n)
            break
        x,r = divmod(n,i)
        if r==0:
            fact.append(i)
            n=x
            rn = sqrt(n)+1
        else:
            i += 2

    res = dict()
    for k in set(fact):
        res[k] = fact.count(k)

    return fact

#print(factor(100))

#Q3
def getFactors(a):
    factors = list()
    for i in range(1,a+1):
        if a%i == 0:
            factors.append(i)
    return factors

def order(a, p, factors_p_minus1):
    """
    :param a: entier positif
    :param p: Z/pZ nombre premier
    :param factors_p_minus1: fact(p-1)
    :return: ordre de a dans Z/pZ
    utiliser pohlig hellman
    """
    if a == 1:
        return 1
    for i in getFactors(p-1):
        if exp(a,i,p) == 1:
            return i


#print(getFactors(880))
#print(order(4, 881, factor(880)))



#Q4
def find_generator(p, factors_p_minus1):
    return


#Q5
def generate_safe_prime(k):
    return


#Q6
def bsgs(n, g, p):
	s = math.ceil(math.sqrt(n))
	
	BS =dict()
	BS[0] = 1
	GS = dict()
	GS[0] = p

	tmpg = g
	
	for i in range(1,s):
		BS[i] = g%n
		g=g*tmpg

	G = inv_mod(g,n)
	tmpG=G	
	for j in range(1,s):
		GS[j] = (p*G)%n 
		G= G*tmpG
		

	BS = sorted(BS.items(), key=lambda t: t[1])
	GS = sorted(GS.items(), key=lambda t: t[1])
	
	resi = 0
	resj = 0

	for i in BS:
		for j in GS : 
			if i[1] == j[1]:
				resi = i[0]
				resj = j[0]
			if  i[1] < j[1]:
				break
		
	print(GS)
	return resi + (s* resj) 


print(bsgs(23,11,3))

#Q8
def next(x, a, b, n, h, p):
    return


#Q9
def rho_pollard(n, h, q, p):
    return
