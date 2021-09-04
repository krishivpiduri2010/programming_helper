import pygame

WIDTH = 600
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)


def main():
    run = True
    mouse_btn_dwn = False
    clock = pygame.time.Clock()
    WIN.fill(WHITE)
    radius = 10
    while run:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
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
        if mouse_btn_dwn:
            pygame.draw.circle(WIN, (0, 0, 0), pygame.mouse.get_pos(), radius)


if __name__ == '__main__':
    main()
