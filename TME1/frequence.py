

def frequence(file):
    f = open(file, "r")
    text = f.read()
    
    cpt=0
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    list =[]
    for i in range(len(alphabet)):
        list.append( (text.count(alphabet[i]) *1.0 ) / len(text))
        
    print(len(text))
    print(list)
    f.close()
    return list

	


#test
#print(frequence("germinal.txt"))
