#Viris
import os

def ekri_nan_fichye_yo(message="You have been hacked",nomfichye= ""):
    file = open(nomfichye, "w")
    file.write(message)
    file.close()

nbr = 1
list_file = []
while nbr <= 5 :
    nomfichye = f"C:/Users/{os.getlogin()}/virus-" + str(nbr)
    ekri_nan_fichye_yo(nomfichye = nomfichye)
    list_file.append(nomfichye)
    nbr+=1
import antivirus