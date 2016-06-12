from PIL import Image, ImageDraw
import sys, math

def f(x1, x2, mode):
    if (mode == 'grey'):
        res = 128 + (x2 - x1) / 2
        if (res < 0):
            res = 0
        elif (res > 255):
            res = 255
        else:
            res = round(res)
    elif (mode == 'black'):
        res = round(abs(x2 - x1))
    return res

image1 = Image.open(input("Путь к изображению 1: ")).convert("RGB")
image2 = Image.open(input("Путь к изображению 2: ")).convert("RGB")
mode = input("Режим: ")
if (image1.size != image2.size):
    print("Разный размер изображений!")
    sys.exit()
(width, height) = image1.size
pix1 = image1.load()
pix2 = image2.load()
diff = Image.new("RGB", image1.size, "white")
draw = ImageDraw.Draw(diff)
for i in range(width):
    for j in range(height):
        (r1, g1, b1) = pix1[i, j]
        (r2, g2, b2) = pix2[i, j]
        draw.point((i, j), (f(r1, r2, mode), f(g1, g2, mode), f(b1, b2, mode)))
diff.save("diff.png")
print("Сделано!")
del draw
