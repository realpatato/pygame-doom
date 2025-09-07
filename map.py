''' IMPORTS '''
import pygame

global wall_colors 
wall_colors = {
    "0" : (0, 0, 0),
    "1" : (255, 255, 255),
    "2" : (255, 0, 0),
    "3" : (255, 255, 0)
}

class Map:
    def __init__(self, level, screen):
        self._level = level
        self._map_display = self.gen_map(screen)

    def gen_map(self, screen):
        #creates empty surface to draw map on
        surface = pygame.Surface((screen.get_width(), screen.get_height()))
        for row in range(len(self._level)):
            for col in range(len(self._level[row])):
                pygame.draw.rect(surface, wall_colors[str(self._level[row][col])], ((col * 10) + 400, (row * 10) + 400, 10, 10))
        return surface
    