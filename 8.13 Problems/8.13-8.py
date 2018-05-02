import cImage as image

img = image.Image("testimage.gif")

width = img.getWidth()
height = img.getHeight()

win = image.ImageWin(img.getWidth(),img.getHeight())

print("Image is ", width, " X ", height)

for Wpx in range (width):
    for Hpx in range (height):
        p = img.getPixel(Wpx,Hpx)

        newRed = 255-p.getRed()
        newGreen = 255-p.getGreen()
        newBlue = 255-p.getBlue()

        newPixel = image.Pixel(newRed,newGreen,newBlue)

        img.setPixel(Wpx,Hpx,newPixel)

img.draw(win)
