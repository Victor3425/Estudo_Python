import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações do labirinto
width, height = 600, 400
cell_size = 20
rows = height // cell_size
cols = width // cell_size

# Cores
white = (255, 255, 255)
black = (0, 0, 0)

# Definição do labirinto (0 para caminho, 1 para parede)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Inicialização da janela
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Labirinto")

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Desenhar o labirinto
    screen.fill(white)
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:
                pygame.draw.rect(screen, black, (j * cell_size, i * cell_size, cell_size, cell_size))

    # Atualizar a tela
    pygame.display.flip()
