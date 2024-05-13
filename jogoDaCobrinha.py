import pygame
from pygame.locals import *
from random import randint

largura, altura = 800, 800

def on_grid_random(largura, altura):
    x = randint(0, largura - 1)
    y = randint(0, altura - 1)
    return (x // 20 * 20, y // 20 * 20)

def colisao(c1, c2):
    return(c1[0] == c2[0]) and (c1[1] == c2[1])

def atualizaTexto(pontos):
    texto = fonte.render(f'Pontos: {pontos}', True, (255, 255, 255))
    tela.blit(texto, (largura - 200, 50))

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()

tela = pygame.display.set_mode((largura, altura), FULLSCREEN, 32)
pygame.display.set_caption('Jogo da cobrinha')

cobra = [(200, 200), (210, 200), (220, 200)]
cobra_skin = pygame.Surface((20, 20))
cobra_skin.fill((0, 80, 0))

fruta_pos = on_grid_random(largura, altura)
fruta = pygame.Surface((20, 20))
fruta.fill((150, 0, 0))

direcaoCobra = LEFT

clock = pygame.time.Clock()

pontos = 0

fonte = pygame.font.Font('fontes/SpaceGrotesk.ttf', 32)

while True:
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if (event.key == K_UP or event.key == K_w) and direcaoCobra != DOWN:
                direcaoCobra = UP
            if (event.key == K_DOWN or event.key == K_s) and direcaoCobra != UP:
                direcaoCobra = DOWN
            if (event.key == K_LEFT or event.key == K_a) and direcaoCobra != RIGHT:
                direcaoCobra = LEFT
            if (event.key == K_RIGHT or event.key == K_d) and direcaoCobra != LEFT:
                direcaoCobra = RIGHT

    if colisao(cobra[0], fruta_pos):
        fruta_pos = on_grid_random(largura, altura)
        cobra.append((0, 0))
        pontos += 1

    for posCobra in cobra[1:]:
        if colisao(cobra[0], posCobra):
            cobra = [(200, 200), (210, 200), (220, 200)]
            cobra_skin = pygame.Surface((20, 20))
            cobra_skin.fill((0, 80, 0))
            direcaoCobra = RIGHT
            pontos = 0

    for i in range(len(cobra) - 1, 0, -1):
        cobra[i] = (cobra[i - 1][0], cobra[i - 1][1])

    if direcaoCobra == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 20)
    if direcaoCobra == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 20)
    if direcaoCobra == RIGHT:
        cobra[0] = (cobra[0][0] + 20, cobra[0][1])
    if direcaoCobra == LEFT:
        cobra[0] = (cobra[0][0] - 20, cobra[0][1])

    tela.fill((0, 0, 0))

    tela.blit(fruta, fruta_pos)
    for pos in cobra:
        tela.blit(cobra_skin, pos)

    atualizaTexto(pontos)

    if cobra[0][0] < 0:
        cobra[0] = (cobra[0][0] + largura, cobra[0][1])
    elif cobra[0][0] >= largura:
        cobra[0] = (cobra[0][0] - largura, cobra[0][1])
    elif cobra[0][1] < 0:
        cobra[0] = (cobra[0][0], cobra[0][1] + altura)
    elif cobra[0][1] >= altura:
        cobra[0] = (cobra[0][0], cobra[0][1] - altura)

    pygame.display.update()