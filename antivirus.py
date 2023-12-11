import virus as v
import os

code = "virus10"
test = True
if os.path.exists(v.nomfichye):

    # Retire fichye yo
    kod = input("CODE ANTIVIRUS :   ")
    if kod == code:
        test = True
        for r in v.list_file:
            os.remove(r)
    else:
        print("----- 3 tentatives -----")
        nbr = 0
        while nbr < 3 and kod != code:
            kod = input("CODE ANTIVIRUS :   ")
            if kod == code:
                test = True
                for j in v.list_file:
                    os.remove(j)
                break
            else:
                test = False
            nbr += 1

    if test == False :
        print("You have been hacked")
    else :
        print("Virus yo siprime, ou gen chans ti baz")
        file = "rescue.txt"
        if os.path.exists(file):
            fichier = open(file, "r")
            n = len(fichier.read().split(","))
            fichier.close()

            fichier = open(file, "a")
            fichier.write(f"{(n)},")
            fichier.close()


