import cImage as image

img = image.Image("testimage.gif")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(0)   # setDelay(0) turns off animation

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        newred = p.getRed()/4
        newgreen = p.getGreen()/4
        newblue = p.getBlue()/4

        newpixel = image.Pixel(newred, newgreen, newblue)

        img.setPixel(col, row, newpixel)

img.draw(win)
win.exitonclick()
