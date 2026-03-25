def conversion1(piece : str):
    match piece:
        case "R" :
            return 50
        case "N" :
            return 30
        case "B" :
            return 31
        case "Q" :
            return 90
        case "K" :
            return 1000
        case "P" :
            return 10
        case "r" :
            return -50
        case "n" :
            return -30
        case "b" :
            return -31
        case "q" :
            return -90
        case "k" :
            return -1000
        case "p" :
            return -10
    return "NB"

print(conversion1("k"))
print(conversion1("B"))
print(conversion1("5"))

def conversionall(fen:str):
    lignes :list[str] = fen.split("/")
    print(lignes)
    echequier : list[list[int]] = [[0 for _ in range(8)] for _ in range(8)]
    chiffre : int = 0 #La ligne aux echecs
    for ligne in lignes:
        lettre : int = 0 #La colonne aux echecs
        for elem in ligne :
            print("chiffre: ", chiffre)
            print("lettre:", lettre)
            convertion = conversion1(elem)
            if convertion == "NB":
                lettre += int(elem)
            else:
                echequier[chiffre][lettre] =  convertion
                lettre += 1
            print(echequier)
        chiffre += 1
    return echequier

print(conversionall('4r1k1/p1p2pp1/1q1p3p/1P3P2/1P6/2n1Q3/PB4PP/4R1K1'))