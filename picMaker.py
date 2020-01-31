import random

def makePic():
    f = open("image.ppm", "w")
    f.write("P3 500 500 255\n")

    i = 0
    while (i < 5):
        patchRow = ""
        j = 0
        while(j < 5):
            r = random.randint(100, 250)
            g = random.randint(0, 200)
            b = random.randint(50, 200)
            patchRow += (str(r) + " " + str(g) + " " + str(b) + " ") * 100
            j += 1
        f.write((patchRow + "\n" )* 100 )
        i += 1
    f.close()

makePic()
