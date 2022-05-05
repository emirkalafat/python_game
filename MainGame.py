import random
import sys
from tkinter import messagebox
import pygame
from tkinter import *

pygame.init()
class Plat:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Tanımlar
Rmavi = (119, 224, 255)
Rsiyah = (0, 0, 0)
GENISLIK = 500
YUKSEKLIK = 700
arkaplanRengi = Rmavi
oyuncuResmi = pygame.transform.scale(pygame.image.load('assest/karakter.png'), (80, 80))
platformResmi = pygame.transform.scale(pygame.image.load('assest/platform.png'), (80, 10))
genel_font = pygame.font.Font('assest/futurab.ttf', 16)
fps = 60
oyuncuIsmi = "Oyuncu1"

root = Tk()
root.title('İsim Girişi')
root.geometry("300x75+300+200")

def retrieve_input():
    global oyuncuIsmi
    oyuncuIsmi = textBox.get("1.0", "end-1c")
    messagebox.showinfo('Hoş Geldiniz.',f'İsminiz {oyuncuIsmi} olarak belirlendi.\nEğer arkaplan rengi hoşunuza gitmezse \'C\' tuşuna basınız.')
    root.destroy()
    print(oyuncuIsmi)

baslik = Label(root, text='İsminizi Giriniz')
baslik.pack()
textBox = Text(root, height=1, width=20)
textBox.pack()
tus = Button(root, height=1, width=10, text="Giriş", command=lambda: retrieve_input())
tus.pack()

mainloop()

def seviyeAdi(seviye):
    switcher = {
        0: "easy",
        1: "normal",
        2: "hard",
        3: "extreme",
    }
    return switcher.get(seviye,"nothing")

def arkaplanRengiDegistir():
    global arkaplanRengi
    arkaplanRengi = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))

# EKRAN
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption('Among Platforms')
# Platformlar
platformlar = [Plat(random.randrange(0, GENISLIK - 80), random.randrange(0, YUKSEKLIK)) for i in range(10)]
# Baslangıç Değerleri
x = 200
y = 100
dy = 0.0
h = 200
ziplama = -20
# puanlar
puan = 0
ziplamaPuan = 0
renkPuan = 0
platformPuan = 0
# # #
tickCheck = 0
superZiplamaHakki = 0
superZiplamaUseTime = 0
gameOver = False

while True:
    tickCheck += 1
    if tickCheck == 60:
        tickCheck = 0
    pygame.time.Clock().tick(fps)
    olaylar = pygame.event.get()
    for olay in olaylar:
        if olay.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ekran.fill(arkaplanRengi)

    if not gameOver:
        for platform in platformlar:
            ekran.blit(platformResmi, (platform.x, platform.y))

        # karakter zeminin en altına indiğinde game over
        if y > YUKSEKLIK:
            gameOver = True

        # oyuncunun sağa sola hareketi #
        tuslar = pygame.key.get_pressed()
        if tuslar[pygame.K_LEFT]:
            x -= 10
            oyuncuResmi = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assest/karakter.png'), (80, 80)),True,False)
        if tuslar[pygame.K_RIGHT]:
            x += 10
            oyuncuResmi = pygame.transform.scale(pygame.image.load('assest/karakter.png'), (80, 80))
        if x < -40:
            x = -40
        if x > GENISLIK - 40:
            x = GENISLIK - 40

        # platformların aşağı yönde hareketi #
        if y < h:
            y = h
            for platform in platformlar:
                platform.y = platform.y - dy
                if platform.y > YUKSEKLIK:
                    platform.y = 0
                    platform.x = random.randrange(0, GENISLIK - 80)
                    puan += 1
                    ziplamaPuan += 1
                    renkPuan += 1
                    platformPuan += 1
        # platformalın her 90 puanda azalması #
        if len(platformlar) >= 5:
            if platformPuan == 90:
                platformlar.pop()
                platformPuan = 0

        # ekran reniginin her 30 puanda değişmesi
        if renkPuan == 30:
            arkaplanRengiDegistir()
            renkPuan = 0
        # beğenilmeyen arkaplan renginin değiştirilmesi #
        if tuslar[pygame.K_c] and tickCheck % 10 == 0:
            arkaplanRengiDegistir()

        # Süper Zıplama #
        if ziplamaPuan == 60:
            superZiplamaHakki += 1
            ziplamaPuan = 0

        if tuslar[pygame.K_SPACE] and superZiplamaHakki > 0 and tickCheck % 10 == 0:
            ziplama = -30
            superZiplamaHakki -= 1
            superZiplamaUseTime = 180

        if ziplama < -20 and superZiplamaUseTime > 0:
            superZiplamaUseTime -= 1

        if ziplama < -20 and superZiplamaUseTime == 0:
            ziplama = -20

        dy += .7
        y += dy

        # karakterin platformlar ile teması #
        for platform in platformlar:
            if (x + 60 > platform.x) and (x + 20 < platform.x + 72) and (y + 74 > platform.y) and (y + 74 < platform.y + 20) and dy > 0:
                dy = ziplama

        # EKRANDA YAZACAK YAZILAR #
        yaziSkor = genel_font.render("Puan " + str(puan), 1, (0, 0, 0))
        yaziSuperZiplama = genel_font.render("Süper Zıplama Hakkı " + str(superZiplamaHakki), 1, (0, 0, 0))
        yaziSuperZiplamaTime = genel_font.render("Süper Zıplama Süresi " + str(superZiplamaUseTime), 1, (0, 0, 0))
        yaziZorlukSeviyesi = genel_font.render("Seviye: " + seviyeAdi((len(platformlar)-10)*(-1)), 1, (0, 0, 0))
        # YAZILARIN EKRANA YAZDIRILMASI #
        ekran.blit(yaziSkor, (GENISLIK - 10 - yaziSkor.get_width(), 10))
        ekran.blit(yaziSuperZiplama, (10, 10))
        if superZiplamaUseTime > 0:
            ekran.blit(yaziSuperZiplamaTime, (10, 30))
        ekran.blit(yaziZorlukSeviyesi,(10,50))
        ekran.blit(oyuncuResmi, (x, y))
    else:
        yaziGameOver = genel_font.render("GAME OVER", 1, (0, 0, 0))
        yaziReset = genel_font.render("yeniden oynamak için 'Boşluk' tuşuna basınız", 1, (0, 0, 0))
        yaziGameOverPuan = genel_font.render(oyuncuIsmi + "'nin puanı " + str(puan), 1, (0, 0, 0))
        ekran.blit(yaziGameOver, (170, 300))
        ekran.blit(yaziGameOverPuan, (160, 330))
        ekran.blit(yaziReset, (50, 550))
        tuslar = pygame.key.get_pressed()
        if tuslar[pygame.K_SPACE]:
            x = 200
            y = 100
            dy = 0.0
            h = 200
            ziplama = -20
            # puanlar
            puan = 0
            ziplamaPuan = 0
            platformPuan = 0
            renkPuan = 0
            # # #
            superZiplamaHakki = 0
            superZiplamaUseTime = 0
            gameOver = False
            platformlar = [Plat(random.randrange(0, GENISLIK - 80), random.randrange(0, YUKSEKLIK)) for i in range(10)]

    pygame.display.update()
