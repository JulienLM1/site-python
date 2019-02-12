import markdown
import os

print('1 - Installation du package markdown')
print('2 - Conversion du fichier markdown')
menu = int(input())

if menu == 1:
    print("Installation du package markdown qui fera la conversion")
    os.system("pip install markdown")

elif menu == 2:
    print("Conversion du fichier markdown vers un fichier html")
    fichier = input("Inserer le fichier markdown a convertir (files.md) : ")
    os.system("python -m markdown -x" + fichier + " > index.html")
