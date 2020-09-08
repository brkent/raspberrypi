from PIL import Image 
import numpy as np

"""
Science and Computing with Raspberry Pi
Brian R. Kent
"""

def combineImages(rgbfiles):

    RGB = []
    
    for i, filename in enumerate(rgbfiles):
        im = Image.open(filename)
        implane = np.array(list(im.getdata()), dtype="uint8")
        reshape = implane.reshape(im.size[0], im.size[1])
        RGB.append(Image.fromarray(reshape,mode=None))

    combine = Image.merge("RGB",(RGB[0],RGB[1],RGB[2]))
    combine.show()
    combine.save("jupiter.png")


combineImages(['junored.png','junogreen.png','junoblue.png'])