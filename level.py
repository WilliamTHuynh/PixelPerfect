import pygame
import os
from mask_functions import level_file_to_mask, \
    level_file_to_mask_inverse, \
    find_color_location


class Levels:
    def __init__(self):
        # Loading Levels into list of Levels
        self.levels = os.listdir(os.getcwd() + '/levels')
        # Loads first level into full level
        self.full_level = "levels/" + self.levels[0]
        self.level_surface = pygame.image.load(self.full_level)
        self.boundary_mask = level_file_to_mask(self.full_level,
                                                (0, 89, 162),
                                                (255, 255, 255),
                                                (245, 130, 32))
        self.finish_mask = level_file_to_mask_inverse(self.full_level,
                                                      (0, 89, 162))

        self.current = 0
        self.start = find_color_location(pygame.image.load(self.full_level),
                                   (245, 130, 32))

    def update(self):
        self.current += 1
        self.full_level = "levels/" + self.levels[self.current]
        self.boundary_mask = level_file_to_mask(self.full_level,
                                                (0, 89, 162),
                                                (255, 255, 255),
                                                (245, 130, 32))
        self.finish_mask = level_file_to_mask_inverse(self.full_level,
                                                      (0, 89, 162))
        return find_color_location(pygame.image.load(self.full_level),
                                   (245, 130, 32))
