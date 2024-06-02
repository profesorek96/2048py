import pygame


class Tile:
    def __init__(self, x, y, color, value, size, font_color):
        self.__rect = pygame.Rect(x, y, size, size)
        self.color = color
        self.font_color = font_color
        self.__font_size = int((self.__rect.size[0] * 0.75))
        self.__font_name = 'freesansbold.ttf'
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

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
        self.__font_resize()

    @property
    def font_color(self):
        return self.__font_color

    @font_color.setter
    def font_color(self, value):
        self.__font_color = value

    def move_left(self, offest):
        self.__rect.x -= offest

    def move_right(self, offest):
        self.__rect.x += offest

    def move_up(self, offest):
        self.__rect.y -= offest

    def move_down(self, offest):
        self.__rect.y += offest

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.__rect)
        font = pygame.font.Font(self.__font_name, self.__font_size)
        text = font.render(f'{self.value}', True, self.font_color)
        font_rect = text.get_rect()
        font_rect.center = self.__rect.center
        surface.blit(text, font_rect)
