from PIL import Image
from tkinter import Tk, filedialog
root = Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
img = Image.open(file_path)
width, height = img.size
pixels = [[0 for x in range(width)] for y in range(height)]
for y in range(height):
    for x in range(width):
        pixels[y][x] = img.getpixel((x, y))
import random
import string
file_name = "".join(random.sample(string.ascii_letters+string.digits, 15))
command = f'''import pygame
def get_surface():
    surface = pygame.Surface({img.size}, pygame.SRCALPHA, 32)'''
for y, row in enumerate(pixels):
    for x, col in enumerate(row):
        if col[3] <= 3:
            continue
        command += f'''
    r, g, b, a = {col}
    square_surface = pygame.Surface((1,1), pygame.SRCALPHA)
    square_surface.fill((r,g,b)); square_surface.set_alpha(a); surface.blit(square_surface, ({x},{y}))'''
command += "\n    return surface"
open("output_"+file_name+".py", "w").write(command)