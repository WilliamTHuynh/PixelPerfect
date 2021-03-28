import pygame
import sys
from box import Box
from mask_functions import level_file_to_mask, \
    level_file_to_mask_inverse, \
    find_color_location
from game_settings import Settings
from level import Levels


pygame.init()
mainClock = pygame.time.Clock()
pygame.mixer.init()
pygame.mixer.music.load('Kahoot Lobby Music.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(loops=-1)
# Set up window
settings = Settings()
WINDOW_WIDTH = settings.screen_width
WINDOW_HEIGHT = settings.screen_height
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Pixel Perfect')


# white color
color = (255, 255, 255)
# light shade of the button
color_light = (170, 170, 170)
# dark shade of the button
color_dark = (100, 100, 100)

# defining a font
startingFont = pygame.font.SysFont('Calibri', 35)

# rendering a text written in
# this font
text = startingFont.render('start', True, color)
gameName = startingFont.render('Pixel Perfect', True, color)
instructions = startingFont.render('Use the arrow keys to move!', True, color)
instructions2 = startingFont.render('Double click start to start!', True, color)
teamName = startingFont.render('By Team CSULF:', True, color)
teamName2 = startingFont.render('William Huynh, Kenny Giang, & Jake Sichley', True, color)
startingState = True
while startingState:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
            # if the mouse is clicked on the
            # button the game is terminated
            if WINDOW_WIDTH / 2 <= mouse[0] <= WINDOW_WIDTH / 2 + 140 and WINDOW_HEIGHT / 2 <= mouse[1] <= WINDOW_HEIGHT / 2 + 40:
                startingState = False
                # fills the screen with a color
    window_surface.fill((0, 89, 162))

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
    if WINDOW_WIDTH / 2 <= mouse[0] <= WINDOW_WIDTH / 2 + 140 and WINDOW_HEIGHT / 2 <= mouse[1] <= WINDOW_HEIGHT / 2 + 40:
        pygame.draw.rect(window_surface, color_light, [WINDOW_WIDTH/ 2, WINDOW_HEIGHT / 2, 140, 40])

    else:
        pygame.draw.rect(window_surface, color_dark, [WINDOW_WIDTH/ 2, WINDOW_HEIGHT / 2, 140, 40])

        # superimposing the text onto our button

    window_surface.blit(text, (WINDOW_WIDTH / 2 + 42, WINDOW_HEIGHT / 2))
    window_surface.blit(gameName, (WINDOW_WIDTH / 100, WINDOW_HEIGHT / 6))
    window_surface.blit(instructions, (5, 500))
    window_surface.blit(instructions2, (5, 560))
    window_surface.blit(teamName, (WINDOW_WIDTH / 100, WINDOW_HEIGHT / 4))
    window_surface.blit(teamName2, (WINDOW_WIDTH / 100, WINDOW_HEIGHT / 3))
    # updates the frames of the game
    pygame.display.update()

levels = Levels()
box = Box(screen=window_surface, speed=settings.player_speed, start=levels.start)

box_mask = pygame.mask.from_surface(box.image)

start = find_color_location(pygame.image.load(levels.full_level), (245, 130, 32))

box.x = start[0]
box.y = start[1]

while True:
    window_surface.blit(pygame.image.load(levels.full_level), (0, 0))
    box.update()
    box.blitme()

    pygame.display.flip()

    mainClock.tick(60)

    if levels.boundary_mask.overlap(box_mask, (box.rect.x, box.rect.y)):
        box.x = start[0]
        box.y = start[1]

    if levels.finish_mask.overlap(box_mask, (box.rect.x, box.rect.y)):
        start = levels.update()
        box.x = start[0]
        box.y = start[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # Change the keyboard variables.
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                box.moving_right = False
                box.moving_left = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                box.moving_left = False
                box.moving_right = True
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                box.moving_down = False
                box.moving_up = True
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                box.moving_up = False
                box.moving_down = True

        if event.type == pygame.KEYUP:
            # Change the keyboard variables.
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                box.moving_left = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                box.moving_right = False
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                box.moving_up = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                box.moving_down = False
