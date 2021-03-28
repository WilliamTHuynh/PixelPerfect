import pygame
from PIL import Image


def level_file_to_mask(path, color1, color2, color3):
    img = Image.open(path)
    img = img.convert("RGBA")
    img_data = img.getdata()

    new_data = []
    for item in img_data:
        if (item[0] == color1[0] and item[1] == color1[1] and item[2] == color1[2]) or\
           (item[0] == color2[0] and item[1] == color2[1] and item[2] == color2[2]) or \
           (item[0] == color3[0] and item[1] == color3[1] and item[2] == color3[2]):
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save('test.png')

    mode = img.mode
    size = img.size
    data = img.tobytes()

    return pygame.mask.from_surface(pygame.image.fromstring(data, size, mode))


def level_file_to_mask_inverse(path, color1):
    img = Image.open(path)
    img = img.convert("RGBA")
    img_data = img.getdata()

    new_data = []
    for item in img_data:
        if item[0] == color1[0] and item[1] == color1[1] and item[2] == color1[2]:
            new_data.append(item)
        else:
            new_data.append((0, 0, 0, 0))

    img.putdata(new_data)
    img.save('test2.png')

    mode = img.mode
    size = img.size
    data = img.tobytes()

    return pygame.mask.from_surface(pygame.image.fromstring(data, size, mode))


def find_color_location(surface, color):
    x1, y1 = surface.get_rect()[2:]

    for x in range(x1):
        for y in range(y1):
            if surface.get_at((x, y))[:3] == color:
                return x, y

    return -1, -1
