#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:22:26 2019

@author: 3679785
"""
import frequence
import cesar
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"




def cryptanalyse_cesar(file):
    freq= frequence.frequence(file)
    max=freq[0]
    ind=0
    for i in range(len(freq)):
        if (max<freq[i]) :
            max= freq[i]
            ind = i
            
    rot = ind - cesar.index('E')
    
    f = open(file, "r")
    text = f.read()
    
    print(cesar.dechiffrer_cesar(text, alphabet[rot]))
    

cryptanalyse_cesar("cesar.txt")