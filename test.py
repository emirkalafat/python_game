import pygame

pygame.init()
##Tanımlar
Rmavi= (119, 224, 255)
Rsiyah= (0,0,0)
GENISLIK = 500
YUKSEKLIK = 700
arkaplanRengi = Rmavi
oyuncu = pygame.transform.scale(pygame.image.load('karakter.png'),(80,80))
fps = 60
genel_font = pygame.font.Font('futurab.ttf',16)
sayac = pygame.time.Clock()

##Değişkenler
karakter_konum_x = 200
karakter_konum_y = 550
platformlar = [[200,650,80,10],[150,550,80,10],[300,450,80,10]]
zipliyorMu = False
y_change = 0
x_change = 0
karakter_hizi = 5

#EKRAN
ekran = pygame.display.set_mode([GENISLIK,YUKSEKLIK])
pygame.display.set_caption('Emir Ebrar the Game')

#functions
def karakteri_guncelle(konum_y):
    global zipliyorMu
    global y_change
    ziplama_boyutu = 15
    yercekimi = .5
    if zipliyorMu:
        y_change = -ziplama_boyutu
        zipliyorMu = False
    konum_y += y_change
    y_change += yercekimi
    return konum_y

def tas_degiyorMu(tas_listesi, j):
    global karakter_konum_x
    global karakter_konum_y
    global y_change #karakter yukarı mı gidiyor aşağı mı gdiyor kontrolü
    for a in range(len(tas_listesi)):
        for i in tas_listesi:
            if i[a].colliderect([karakter_konum_x, karakter_konum_y + 60, 80 ,10]) and j == False and y_change > 0:
                j = True
    return j

##burada baştan denemye çalıştım yine olmadı ilk taşa zıplıyor diğerlerine zıplamıyor
##sinir oldum

calisiyorMu = True
while calisiyorMu == True:
    sayac.tick(fps)
    ekran.fill(arkaplanRengi)
    ekran.blit(oyuncu,(karakter_konum_x,karakter_konum_y))
    taslar = [[]]

    for i in range(len(platformlar)):
        tas = pygame.draw.rect(ekran,Rsiyah,platformlar[i],0,3)
        taslar.append(tas)

    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            calisiyorMu = False
        if olay.type == pygame.KEYDOWN:
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
    karakter_konum_y = karakteri_guncelle(karakter_konum_y)

    pygame.display.flip()
pygame.quit()
