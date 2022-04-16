import pygame

pygame.init()
##Tanımlar
renk1= (119,224,255)
GENISLIK = 500
YUKSEKLIK = 700
arkaplanRengi = renk1
##
oyuncu = pygame.image.load('karakter.png')
fps = 60
genel_font = pygame.font.Font('futurab.ttf',16)
sayac = pygame.time.Clock()

#EKRAN

ekran = pygame.display.set_mode([GENISLIK,YUKSEKLIK])
pygame.display.set_caption('Emir Ebrar the Game')

calisiyorMu = True
while calisiyorMu == True:
    sayac.tick(fps)
    ekran.fill(arkaplanRengi)

    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            calisiyorMu = False

    pygame.display.flip()
pygame.quit()