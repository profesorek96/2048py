import pygame
import constants


class Tile:
    def __init__(self, x, y, value, size):
        self.__rect = pygame.Rect(x, y, size, size)
        self.__color = constants.TilesColor.get_tile_color(value)
        self.__font_color = constants.TilesColor.get_font_color(value)
        self.__font_size = int((self.__rect.size[0] * 0.75))
        self.__font_name = constants.FONT_NAME
        self.value = value

    def __font_resize(self):
        text_rect = self.__rect.size
        k = 0.75
        while text_rect[0] >= self.__rect.size[0] or text_rect[1] >= self.__rect.size[1]:
            self.__font_size = int((self.__rect.size[0] * k))
            font = pygame.font.Font(self.__font_name, self.__font_size)
            text = font.render(f'{self.value}', True, (0, 0, 0))
            text_rect = text.get_rect().size
            k -= 0.05
        self.__font_size = int((self.__rect.size[0] * k))
        self.__color = constants.TilesColor.get_tile_color(self.value)
        self.__font_color = constants.TilesColor.get_font_color(self.value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
        self.__font_resize()

    def move_left(self, offset):
        self.__rect.x -= offset

    def move_right(self, offset):
        self.__rect.x += offset

    def move_up(self, offset):
        self.__rect.y -= offset

    def move_down(self, offset):
        self.__rect.y += offset

    def draw(self, surface):
        pygame.draw.rect(surface, self.__color, self.__rect)
        if self.value != 0:
            font = pygame.font.Font(self.__font_name, self.__font_size)
            text = font.render(f'{self.value}', True, self.__font_color)
            font_rect = text.get_rect()
            font_rect.center = self.__rect.center
            surface.blit(text, font_rect)
