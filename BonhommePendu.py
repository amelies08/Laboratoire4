lettre1 = lettre2 = lettre3 = lettre4 = "_" #variables pour montrer le nombre de lettres et l'emplacement des lettres

bonhomme = ["o", "|", "^"] #variables du bonhomme

reponse = ["wham", "cure"]

print("Devine le groupe de musique")
mauvais = 0 #mauvaises reponses

for mot in reponse:
    while (lettre1 != mot[0] or lettre2 != mot[1] or lettre3 != mot[2] or lettre4 != mot[3]) and mauvais < 3: #pendant qu'il y a au moins un lettre qui n'est pas devine et qu'il y a moins de 3 mauvaises reponses
        x = False
        z = False
        while not x or not z: #tant que guess n'est pas une lettre et qu'il n'y a pas seulement une lettre
            guess = input() #devine la lettre
            x = guess.isalpha() #est-ce que guess est une lettre
            z = len(guess) == 1 #est-ce qu'il y a seulement une lettre
        if guess == mot[0]: #si la lettre devinee est une des lettres du mot
            lettre1 = mot[0] #remplace la ligne par la lettre au bon emplacement
            print("bonne reponse")
        elif guess == mot[1]:
            lettre2 = mot[1]
            print("bonne reponse")
        elif guess == mot[2]:
            lettre3 = mot[2]
            print("bonne reponse")
        elif guess == mot[3]:
            lettre4 = mot[3]
            print("bonne reponse")
        else:
            mauvais = mauvais + 1 #changer le nombre de mauvaises reponse lorsque necessaire et inscrire ce nombre
            print("mauvaise reponse")
            if mauvais == 1:
                print(bonhomme[0]) #Ajouter une partie du bonhomme
                if mot == "wham":
                    for y in range(1): #range et y sont egales a 0
                        if y == 0:
                            print("C'est un groupe des années 80.") #montrer premier indice
                            continue
                else:
                    for y in range(1): #range et y sont egales a 0
                        if y == 0:
                            print("C'est un groupe de rock qui a été formé en Angleterre dans les années 70.") #montrer premier indice
                            continue
            else:
                print(bonhomme[0]) #ajouter une autre partie du bohomme
                print(bonhomme[1])
                if mot == "wham":
                    for y in range(1): #range et y sont egales a 0
                        if y == 0:
                            print("Un des membres du groupe a fait de la musique solo par la suite.") #montrer premier indice
                            continue
                else:
                    for y in range(1): #range et y sont egales a 0
                        if y == 0:
                            print("Le chanteur se nomme Robert Smith.") #montrer premier indice
                            continue
        print(lettre1, lettre2, lettre3, lettre4) #ecrire les lettres devoilees et leur emplacements
    else: #s'il y a 3 mauvaises reponses ou que toutes les reponses sont bonnes
        if lettre1 == mot[0] and lettre2 == mot[1] and lettre3 == mot[2] and lettre4 == mot[3] and mauvais < 3: #si toutes les lettres sont devoilees et qu'il y a moins de 3 mauvaises reponses
            print("bravo")
            continuer = input("Voulez-vous continuer?")
            if continuer == "oui":
                lettre1 = lettre2 = lettre3 = lettre4 = "_"
                print(lettre1, lettre2, lettre3, lettre4)
                continue
            elif continuer == "non":
                break
        elif mauvais == 3: #s'il y a 3 mauvaises reponses
            print(bonhomme[0]) #imprime le bonhomme au complet
            print(bonhomme[1])
            print(bonhomme[2])
            print("game over")