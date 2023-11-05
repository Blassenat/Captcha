import string
import random


length = 6
captcha_caractere = string.ascii_letters + string.digits


def generation_captcha(length):
    captcha = ''.join(random.choice(captcha_caractere)for _ in range (length))
    return captcha

captcha = generation_captcha(length)  # Génère un nouveau captcha

def image_captcha():
    from PIL import Image, ImageDraw, ImageFont
    img= Image.new('RGB', (100,30), color = (73,109,137))
    fnt = ImageFont.truetype("times.ttf", 15)
    d = ImageDraw.Draw(img)
    d.text((10,10),captcha, font=fnt, fill=(255,255,0))
    img.save('pil_text_font.png')
def afficher_captcha():
    from PIL import Image
    with Image.open('pil_text_font.png') as img:
        img.show()


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
image_captcha()
resoudre_captcha()

