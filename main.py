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
karakter_konum_x = 170
karakter_konum_y = 400
platformlar = [[175,480,70,10]]

#EKRAN
ekran = pygame.display.set_mode([GENISLIK,YUKSEKLIK])
pygame.display.set_caption('Emir Ebrar the Game')

calisiyorMu = True
while calisiyorMu == True:
    sayac.tick(fps)
    ekran.fill(arkaplanRengi)
    ekran.blit(oyuncu,(karakter_konum_x,karakter_konum_y))

    taslar = []

    for i in range(len(platformlar)):
        tas = pygame.draw.rect(ekran,Rsiyah,platformlar[i])
        taslar.append(tas)


    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            calisiyorMu = False

    pygame.display.flip()
pygame.quit()