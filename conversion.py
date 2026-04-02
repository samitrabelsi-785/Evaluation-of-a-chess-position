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


def conversionall(fen: str):
    lignes = fen.split("/")
    echiquier = []

    for ligne in lignes:
        for elem in ligne:
            convertion = conversion1(elem)
            if convertion == "NB":
                # NB = nombre de cases vides
                echiquier.extend([0] * int(elem))
            else:
                echiquier.append(convertion)

    return echiquier
