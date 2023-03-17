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
command = f'''import pygame as p
z = p.Surface
c = p.SRCALPHA
m = "#000000"
n = "#FFFFFF"
q = 255
def get_surface():
    a = z({img.size}, p.SRCALPHA, 32)
    def d(clr,b,pos):
        s = z((1,1), c)
        s.fill(clr)
        s.set_alpha(b)
        a.blit(s, pos)
    '''
for y, row in enumerate(pixels):
    for x, col in enumerate(row):
        if col[3] <= 3:
            continue
        r, g, b, a = col
        col = f'#{hex(r).removeprefix("0x").rjust(2, "0")}{hex(g).removeprefix("0x").rjust(2, "0")}{hex(b).removeprefix("0x").rjust(2, "0")}'
        if a == 255:
            if col == "#000000":
                command += f'd(m,q,({x},{y}));'
            elif col.lower() == "#ffffff":
                command += f'd(n,q,({x},{y}));'
            else:
                command += f'd({col},q,({x},{y}));'
        else:
            if col == "#000000":
                command += f'd(m,q,({x},{y}));'
            elif col.lower() == "#ffffff":
                command += f'd(n,q,({x},{y}));'
            else:
                command += f'd({col},q,({x},{y}));'
        
command += "\n    return a\n"
command += "if __name__ == \"__main__\":\n"
command +='''
    surface = get_surface()
    window = p.display.set_mode((500, 500))
    window.fill((255,255,255))
    window.blit(surface, (250-int(surface.get_width()/2), 250-int(surface.get_width()/2)))
    while True:
        p.display.update()
'''
open("output_"+file_name+".py", "w").write(command)