def indice_de_masse_corporelle(p, t):
    imc = p / (t ** 2) # Indiquer la formule pour calculer l'IMC.
    print("IMC = {:0.1f}".format(imc))
    if imc <= 18.5:
        print("Valeur d'IMC indiquant une maigreur")
    elif 18.5 < imc <= 24.9 :
        print("Valeur d'IMC normal")
    elif 24.9 < imc <= 29.9 :
        print("Valeur d'IMC indiquant un surpoids")
    elif 29.9 < imc <= 40 :
        print("Valeur d'IMC indiquant un obésité")
    else :
        print("Valeur d'IMC indiquant une obésité massive")
    return imc

imc = indice_de_masse_corporelle(54.2,1.71)