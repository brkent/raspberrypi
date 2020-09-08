from PIL import Image 
import numpy as np
from astropy.io import fits

"""
Science and Computing with Raspberry Pi
Brian R. Kent
"""

def combineImages(rgbfiles):

    RGB = []
    
    for i, filename in enumerate(rgbfiles):
        hdul = fits.open(filename)
        hdu = hdul[0]
        implane = np.array(list(hdu.data), dtype="uint8")
        reshape = implane.reshape(hdu.shape[0], hdu.shape[1])
        RGB.append(Image.fromarray(reshape,mode=None))
        hdul.close

    combine = Image.merge("RGB",(RGB[0],RGB[1],RGB[2]))
    combine.show()
    combine.save("milkyway.png")

combineImages(['halpha.fits','408.fits','mellingerblue.fits'])