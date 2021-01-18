import cv2
from PIL import Image



# ----------------------------------------- compressing using pillow library ----------------------------------------------------------------------------

img = Image.open('pathToImg1')
img2 = Image.open("pathToImg2")

"""
Save the picture with desired quality 
To change the quality of image, 
set the quality variable at 
your desired level, The more  
the value of quality variable  
and lesser the compression 

"""
# using JPG
img.save("compressedImageJPG.jpg", format="JPEG", quality=20)



# using PNG
img2.save("compressedImagePNG.png", format="PNG", quality=10)


# ----------------------------------------- End of compressing using pillow library ----------------------------------------------------------------------------


# ----------------------------------------- compressing using opencv library ----------------------------------------------------------------------------


img = cv2.imread('pathToImg')

"""

The cv2.imwrite function takes three arguments: 
the path of output file, the image itself, 
and the parameters of saving. When saving an image 
to PNG format, we can specify the compression level. 
The value of IMWRITE_PNG_COMPRESSION must be in the (0, 9) 
interval—the bigger the number, the smaller the file on the 
disk, but the slower the decoding process.

"""

# using PNG
cv2.imwrite('compressedOpenCvPNG.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 0]) # save image with lower compression—bigger file size but faster decoding



"""

When saving to JPEG format, we can manage the compression process by setting the value 
of IMWRITE_JPEG_QUALITY. We can set this as any value from 0 to 100. But here, we have 
a situation where bigger is better. Larger values lead to higher result quality and a 
lower amount of JPEG artifacts.

"""

# using JPG
cv2.imwrite('compressedOpenCvPNG.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 0]) # save image with lower quality—smaller file size


# ----------------------------------------- End of compressing using opencv library ----------------------------------------------------------------------------


