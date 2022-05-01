import random
import sys
import pygame

pygame.init()
##Tanımlar
Rmavi = (119, 224, 255)
Rsiyah = (0, 0, 0)
GENISLIK = 500
YUKSEKLIK = 700
arkaplanRengi = Rmavi
oyuncuResmi = pygame.transform.scale(pygame.image.load('karakter.png'), (80, 80))
platformResmi = pygame.transform.scale(pygame.image.load('platform.png'), (80, 10))
genel_font = pygame.font.Font('futurab.ttf', 16)
fps = 60

# EKRAN
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption('Emir Ebrar the Game')

class Plat:
    def __init__(self, x, y):
        self.x = x
        self.y = y

platformlar = [Plat(random.randrange(0,GENISLIK),random.randrange(0,YUKSEKLIK)) for i in range(10) ]
#platformlar = [Plat(250, 450)]
x = 200
y = 100
dy = 0.0
h = 200
ziplama = -20
puan = 0
ziplamaPuan = 0
superZiplamaHakki = 0
superZiplamaUseTime = 0

calisiyorMu = True
while calisiyorMu:
    pygame.time.Clock().tick(fps)
    olaylar = pygame.event.get()
    for olay in olaylar:
        if olay.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ekran.fill(arkaplanRengi)

    for platform in platformlar:
        ekran.blit(platformResmi, (platform.x, platform.y))

    tuslar = pygame.key.get_pressed()
    if tuslar[pygame.K_LEFT]:
        x -= 10
        oyuncuResmi = pygame.transform.flip(pygame.transform.scale(pygame.image.load('karakter.png'), (80, 80)), True, False)
    if tuslar[pygame.K_RIGHT]:
        x += 10
        oyuncuResmi = pygame.transform.scale(pygame.image.load('karakter.png'), (80, 80))

    ###platformların aşağı yönde hareketi###
    if y < h:
        y = h
        for platform in platformlar:
            platform.y = platform.y - dy
            if platform.y > YUKSEKLIK:
                platform.y = 0
                platform.x = random.randrange(0, GENISLIK)
    #######################################

    ###Süper Zıplama###
    if ziplamaPuan == 20:
        superZiplamaHakki += 1
        ziplamaPuan = 0

    if tuslar[pygame.K_SPACE] and superZiplamaHakki > 0:
        ziplama = -30
        superZiplamaHakki -= 1
        superZiplamaUseTime = 180

    if ziplama < -20 and superZiplamaUseTime > 0:
        superZiplamaUseTime -= 1

    if ziplama < -20 and superZiplamaUseTime == 0:
        ziplama = -20
    ##################

    dy += .7
    y += dy

    ###karakterin zeminin en altına indiğinde geri yukarı çıkıması. BURAYI OYUNU KATBETME OLARAK DEĞİŞTİRECEĞİZ!!!!!!!!!
    if y > YUKSEKLIK:
        dy = ziplama

    for platform in platformlar:
        if (x + 60 > platform.x) and (x + 20 < platform.x+72) and (y + 74 > platform.y )and(y + 74 < platform.y + 20) and dy > 0:
            dy = ziplama
            puan += 1
            ziplamaPuan += 1

    ###EKRANDA YAZACAK YAZILAR###
    yaziSkor = genel_font.render("Puan " + str(puan), 1, (0, 0, 0))
    yaziSuperZiplama = genel_font.render("Süper Zıplama Hakkı " + str(superZiplamaHakki), 1, (0, 0, 0))
    yaziSuperZiplamaTime = genel_font.render("Süper Zıplama Süresi " + str(superZiplamaUseTime), 1, (0, 0, 0))

    ###YAZILARIN EKRANA YAZDIRILMASI###
    ekran.blit(yaziSkor, (GENISLIK - 10 - yaziSkor.get_width(), 10))
    ekran.blit(yaziSuperZiplama,(10 , 10))
    if superZiplamaUseTime > 0:
        ekran.blit(yaziSuperZiplamaTime, (10, 30))
    ekran.blit(oyuncuResmi, (x, y))
    ################################

    pygame.display.update()