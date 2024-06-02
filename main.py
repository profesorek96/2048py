import pygame
import tile

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode([1000, 1000])
    pygame.display.set_caption('2048py')

    tile = [tile.Tile(0, 0, (0, 0, 255), 2, 100, (0, 255, 0)),
            tile.Tile(200, 0, (0, 0, 255), 4, 100, (0, 255, 0)),
            tile.Tile(400, 0, (0, 0, 255), 8, 100, (0, 255, 0)),
            tile.Tile(600, 0, (0, 0, 255), 16, 100, (0, 255, 0)),
            tile.Tile(800, 0, (0, 0, 255), 32, 100, (0, 255, 0)),
            tile.Tile(0, 200, (0, 0, 255), 64, 100, (0, 255, 0)),
            tile.Tile(200, 200, (0, 0, 255), 128, 100, (0, 255, 0)),
            tile.Tile(400, 200, (0, 0, 255), 256, 100, (0, 255, 0)),
            tile.Tile(600, 200, (0, 0, 255), 512, 100, (0, 255, 0)),
            tile.Tile(800, 200, (0, 0, 255), 1024, 100, (0, 255, 0))]

    print(pygame.font.get_fonts())
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tile[-1].move_left(50)
                if event.key == pygame.K_RIGHT:
                    tile[-1].move_right(50)
                if event.key == pygame.K_UP:
                    tile[-1].move_up(50)
                if event.key == pygame.K_DOWN:
                    tile[-1].move_down(50)
            elif event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        for i in tile:
            i.draw(screen)

        pygame.display.flip()

    pygame.quit()
