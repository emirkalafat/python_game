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
oyuncu = pygame.transform.scale(pygame.image.load('karakter.png'), (80, 80))
platformResmi = pygame.transform.scale(pygame.image.load('platform.png'),(50,50))
fps = 60
genel_font = pygame.font.Font('futurab.ttf', 16)
sayac = pygame.time.Clock()
# EKRAN
ekran = pygame.display.set_mode([GENISLIK, YUKSEKLIK])
pygame.display.set_caption('Emir Ebrar the Game')
# platform
class Plat:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.uzunluk = 80
        self.kalinlik = 10

platformlar = [[random.randrange(0,GENISLIK),random.randrange(0,YUKSEKLIK),80,10] for i in range(15)]

calisiyorMu = True
while calisiyorMu:
    karakter_konum_x = 200
    karakter_konum_y = 550
    zipliyorMu = False
    y_change = 0
    x_change = 0
    karakter_hizi = 5
    son_puan = 0
    super_ziplama = 2
    son_ziplama = 0
    puan = 0
    yuksek_puan = 0

    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            calisiyorMu = False
    gameover = False
    basilanTus = pygame.key.get_pressed()
    while not gameover:
        for olay in pygame.event.get():
            if olay.type == pygame.QUIT:
                calisiyorMu = False
        karakter_konum_x = 200
        karakter_konum_y = 550
        zipliyorMu = False
        y_change = 0
        x_change = 0
        karakter_hizi = 5
        son_puan = 0
        super_ziplama = 2
        son_ziplama = 0
        puan = 0
        yuksek_puan = 0

        sayac.tick(fps)
        ekran.fill(arkaplanRengi)
        ekran.blit(oyuncu, (karakter_konum_x, karakter_konum_y))

        puan_metni = genel_font.render('High Score:' + str(yuksek_puan), True, Rsiyah, arkaplanRengi)
        ekran.blit(puan_metni, (280, 0))
        yuksek_puan_metni = genel_font.render('Score:' + str(puan), True, Rsiyah, arkaplanRengi)
        ekran.blit(puan_metni, (320, 20))

        puan_metni = genel_font.render('Air Jumps(Spacebar):' + str(yuksek_puan), True, Rsiyah, arkaplanRengi)
        ekran.blit(puan_metni, (10, 10))

        game_over_metni = genel_font.render('GAME OVER: Spacebar to restart!' + str(puan), True, Rsiyah, arkaplanRengi)
        ekran.blit(game_over_metni, (320, 20))
        for olay in pygame.event.get():
            if olay.type == pygame.KEYDOWN:
                if olay.key == pygame.K_a or olay.key == pygame.K_LEFT:
                    x_change = -karakter_hizi
                if olay.key == pygame.K_d or olay.key == pygame.K_RIGHT:
                    x_change = karakter_hizi

        for i in range(len(platformlar)):
            pygame.draw.rect(ekran, Rsiyah,platformlar[i],0,3)

        y_change += 0.2
        karakter_konum_y += y_change
        if karakter_konum_y > YUKSEKLIK:
            dy = -10

        if x_change > 0:
            oyuncu = pygame.transform.scale(pygame.image.load('karakter.png'), (80, 80))
        elif x_change < 0:
            oyuncu = pygame.transform.flip(pygame.transform.scale(pygame.image.load('karakter.png'), (80, 80)), 1, 0)

        if puan > yuksek_puan:
            yuksek_puan = puan

        if puan - son_puan > 10:
            son_puan = puan
            background = (random.randint(1, 255), random.randint(1, 255))

        if puan - son_ziplama > 40:
            son_ziplama = puan
            son_ziplama += 1
    for olay in pygame.event.get():
        if olay == pygame.K_SPACE:
            gameover = False
    pygame.display.flip()
pygame.quit()
#sys.exit()
