def matlistas(matciudades, matEnlz):
    fil = len(matciudades)
    lstdeciudades = [0] * fil
    for f in range(fil):
        lstdeciudades[f] = sum(matciudades[f]) * matEnlz[f]
     
    matciudades = max(lstdeciudades) 
    Enlz = lstdeciudades.index(matciudades) + 1   
    return Enlz

def EnlazCiud():
    
    
    
matEnlz = []
matciudades =[[]]

matciudadesinput("Dijite las ciudades: ")












