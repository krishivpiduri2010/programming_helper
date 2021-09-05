import pygame
pygame.font.init()

WIDTH = 1536
HEIGHT = 801
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT=pygame.font.SysFont('comicsans',40)

WHITE = (255, 255, 255)

# board = [[(255, 255, 255) for i in range(WIDTH)] for i in range(HEIGHT)]


def draw(win: pygame.Surface):
    # win.fill(WHITE)
    # for h, i in enumerate(board):
    #     for k, j in enumerate(i):
    #         pygame.draw.line(WIN, j, (h, k), (h, k))

    pygame.display.update()


def main():
    run = True
    mouse_btn_dwn = False
    clock = pygame.time.Clock()
    WIN.fill(WHITE)
    erase=False
    radius = 10
    while run:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_btn_dwn = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_btn_dwn = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            radius -= 3
        if keys[pygame.K_UP]:
            radius += 3
        if keys[pygame.K_e]:
            erase=not erase
        if mouse_btn_dwn:
            pygame.draw.circle(WIN,(0,0,0) if not erase else (255,255,255),pygame.mouse.get_pos(),radius)
        draw(WIN)


if __name__ == '__main__':
    main()