# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import string
import random

length = 6



captcha_caractere = string.ascii_letters + string.digits


def generation_captcha(length):
    captcha = ''.join(random.choice(captcha_caractere)for _ in range (length))
    return captcha

captcha = generation_captcha(length)  # Stocke le résultat de la génération du captcha dans la variable 'captcha'

def afficher_captcha():
    print(captcha)

def resoudre_captcha():
     reussite = False
     while not reussite:
         afficher_captcha()
         saisie = input("Veuillez entrer le captcha :")

         if saisie == captcha:
                print("Vous avez réussi")
                reussite = True
         else:
                print("Saisie incorrecte, recommencez")


generation_captcha(length)
resoudre_captcha()

