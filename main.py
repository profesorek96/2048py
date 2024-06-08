import pygame
import tile
import constants

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode([1000, 1000])
    pygame.display.set_caption('2048py')

    tile = [tile.Tile(0, 0,  2, 100),
            tile.Tile(200, 0,  4, 100),
            tile.Tile(400, 0,  8, 100),
            tile.Tile(600, 0,  16, 100),
            tile.Tile(800, 0,  32, 100),
            tile.Tile(0, 200,  64, 100),
            tile.Tile(200, 200,  128, 100),
            tile.Tile(400, 200,  256, 100),
            tile.Tile(600, 200,  512, 100),
            tile.Tile(800, 200,  1024, 100),
            tile.Tile(0, 400,  2048, 100),
            tile.Tile(200, 400,  4096, 100),
            tile.Tile(400, 400,  8192, 100),
            tile.Tile(600, 400,  16384, 100),
            tile.Tile(800, 400,  16384*2, 100)]

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

        screen.fill(constants.BG_COLOR)

        for i in tile:
            i.draw(screen)

        pygame.display.flip()

    pygame.quit()
