import random
import pygame

pygame.init()
##Tanımlar
Rmavi = (119, 224, 255)
Rsiyah = (0, 0, 0)
GENISLIK = 500
YUKSEKLIK = 700
arkaplanRengi = Rmavi
oyuncu = pygame.transform.scale(pygame.image.load('karakter.png'), (80, 80))
fps = 60
genel_font = pygame.font.Font('futurab.ttf', 16)
sayac = pygame.time.Clock()

##Değişkenler
karakter_konum_x = 200
karakter_konum_y = 550
ilk_platform = [200, 650, 80, 10]
platformlar = [ilk_platform,[300,410,80,10],[200,390,80,10],[100,190,80,10],[300,190,80,10],[200,40,80,10]]
zipliyorMu = False
y_change = 0
x_change = 0
karakter_hizi = 5

son_puan = 0
super_ziplama = 2
son_ziplama = 0
puan = 0
yuksek_puan = 0
game_over = False

# EKRAN
ekran = pygame.display.set_mode([GENISLIK, YUKSEKLIK])
pygame.display.set_caption('Emir Ebrar the Game')


# functions
def karakteri_guncelle(konum_y):
    global zipliyorMu
    global y_change
    ziplama_boyutu = 20
    yercekimi = .5
    if zipliyorMu:
        y_change = -ziplama_boyutu
        zipliyorMu = False
    konum_y += y_change
    y_change += yercekimi
    return konum_y


# platform hareketi
def platformlari_guncelle(listem, konum_y, change):
    global puan
    if konum_y < 250 and change < 0:
        for i in range(len(listem)):
            listem[i][1] -= change
    else:
        pass
    for item in range(len(listem)):
        if listem[item][1] > 650:  # sayilari degistir
            listem[item] = [random.randint(200, 700), random.randint(0, 200), 80, 10]
            puan += 1
    return listem


def tas_degiyorMu(tas_listesi, jump):
    global karakter_konum_x
    global karakter_konum_y
    global y_change  # karakter yukarı mı gidiyor aşağı mı gdiyor kontrolü
    for i in range(len(tas_listesi)):
        if tas_listesi[i].colliderect(
                [karakter_konum_x, karakter_konum_y + 60, 35, 10]) and jump is False and y_change > 0:
            jump = True
        return jump


calisiyorMu = True
while calisiyorMu == True:
    sayac.tick(fps)
    ekran.fill(arkaplanRengi)
    ekran.blit(oyuncu, (karakter_konum_x, karakter_konum_y))

    taslar = []

    puan_metni = genel_font.render('High Score:' +str(yuksek_puan), True, Rsiyah, arkaplanRengi )
    ekran.blit(puan_metni, (280,0))
    yuksek_puan_metni = genel_font.render('Score:' + str(puan), True, Rsiyah, arkaplanRengi)
    ekran.blit(puan_metni, (320, 20))

    puan_metni = genel_font.render('Air Jumps(Spacebar):' + str(yuksek_puan), True, Rsiyah, arkaplanRengi)
    ekran.blit(puan_metni, (10, 10))
    if game_over:
        game_over_metni = genel_font.render('GAME OVER: Spacebar to restart!' + str(puan), True, Rsiyah, arkaplanRengi)
        ekran.blit(game_over_metni, (320, 20))

    for i in range(len(platformlar)):
        tas = pygame.draw.rect(ekran, Rsiyah, platformlar[i], 0, 3)
        taslar.append(tas)

    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            calisiyorMu = False

        if olay.type == pygame.KEYDOWN:
            if olay.key == pygame.K_SPACE and game_over:
                game_over = False
                puan = 0
                karakter_konum_x = 170
                karakter_konum_y = 400
                background = Rmavi
                son_puan = 0
                super_ziplama = 2
                son_ziplama = 0
                ilk_platform = [200, 650, 80, 10]
                platformlar = [ilk_platform,[300,410,80,10],[200,390,80,10],[100,190,80,10],[300,190,80,10],[200,40,80,10]]
            if olay.key == pygame.K_SPACE and not game_over and super_ziplama > 0:
                super_ziplama -= 1
                y_change = -10
            if olay.key == pygame.K_a or olay.key == pygame.K_LEFT:
                x_change = -karakter_hizi
            if olay.key == pygame.K_d or olay.key == pygame.K_RIGHT:
                x_change = karakter_hizi

        if olay.type == pygame.KEYUP:
            if olay.key == pygame.K_a or olay.key == pygame.K_LEFT:
                x_change = 0
            if olay.key == pygame.K_d or olay.key == pygame.K_RIGHT:
                x_change = 0

    zipliyorMu = tas_degiyorMu(taslar, zipliyorMu)
    karakter_konum_x += x_change

    if karakter_konum_y < 440:
        karakter_konum_y= karakteri_guncelle(karakter_konum_y)
    else:
        game_over=True
        y_change = 0
        x_change = 0

    #karakter_konum_y = karakteri_guncelle(karakter_konum_y)
    platformlar = platformlari_guncelle(platformlar, karakter_konum_y, y_change)
    if karakter_konum_x < -20:
        karakter_konum_x = -20
    elif karakter_konum_x >330:
        karakter_konum_x=330

    if x_change > 0:
        oyuncu = pygame.transform.scale(pygame.image.load('karakter.png'), (80, 80))
    elif x_change < 0:
        oyuncu = pygame.transform.flip(pygame.transform.scale(pygame.image.load('karakter.png'), (80, 80)),1,0)


    if puan > yuksek_puan:
        yuksek_puan= puan


    if puan - son_puan > 10:
        son_puan=puan
        background=(random.randint(1, 255), random.randint(1,255))

    if puan - son_ziplama > 40:
        son_ziplama = puan
        son_ziplama += 1

    pygame.display.flip()
pygame.quit()
