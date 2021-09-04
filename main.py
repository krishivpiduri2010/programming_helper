import pygame

WIDTH = 600
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

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
    clock=pygame.time.Clock()
    WIN.fill(WHITE)

    while run:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_btn_dwn = True
        if mouse_btn_dwn:
            # board[(mouse_pos := pygame.mouse.get_pos())[0]][mouse_pos[1]] = (0, 0, 0)
            # board[(mouse_pos := pygame.mouse.get_pos())[0]+1][mouse_pos[1]] = (0, 0, 0)
            # board[(mouse_pos := pygame.mouse.get_pos())[0]][mouse_pos[1]+1] = (0, 0, 0)
            # board[(mouse_pos := pygame.mouse.get_pos())[0]-1][mouse_pos[1]] = (0, 0, 0)
            # board[(mouse_pos := pygame.mouse.get_pos())[0]][mouse_pos[1]-1] = (0, 0, 0)
            # board[(mouse_pos := pygame.mouse.get_pos())[0]+1][mouse_pos[1]+1] = (0, 0, 0)
            # board[(mouse_pos := pygame.mouse.get_pos())[0]-1][mouse_pos[1]-1] = (0, 0, 0)
            # board[(mouse_pos := pygame.mouse.get_pos())[0]+1][mouse_pos[1]-1] = (0, 0, 0)
            # board[(mouse_pos := pygame.mouse.get_pos())[0]-1][mouse_pos[1]+1] = (0, 0, 0)
            pygame.draw.circle(WIN,(0,0,0),pygame.mouse.get_pos(),60)
        draw(WIN)


if __name__ == '__main__':
    main()
