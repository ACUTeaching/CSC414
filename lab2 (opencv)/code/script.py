import cv2
import numpy as np


# ------------------------------ intro to opencv gui + drawing  ------------------------------------------------

"""

cv2.imread : 
    o what does it do ?  it loads an image from a specified file.
    
    o params :
        * path to the image 
        * flag :  It specifies the way in which image should be read. It’s default value is cv2.IMREAD_COLOR.
            different values for flag param : 
                # cv2.IMREAD_COLOR: It specifies to load a color image. Any transparency of image will be neglected. It is the default flag. Alternatively, we can pass integer value 1 for this flag.
                # cv2.IMREAD_GRAYSCALE: It specifies to load an image in grayscale mode. Alternatively, we can pass integer value 0 for this flag.
                # cv2.IMREAD_UNCHANGED: It specifies to load an image as such including alpha channel. Alternatively, we can pass integer value -1 for this flag.

"""

# img = cv2.imread('/home/mohamed/Pictures/trees (copy).jpg', cv2.IMREAD_UNCHANGED)
# cv2.line(img, (50,50), (150,150), (255,0,0), 8) # img, start point, end point, color as a tuple of BGR, thickness of the line
# cv2.rectangle(img, (0, 0), (200, 150), (0,0,255),-5)
# cv2.circle(img, (100,63), 55, (0,255,0), -1) # negative line width will fill the circle
# cv2.imshow('img', img) # to show the window. It won't show if you don't add it. it takes title of window, the img as parameters


"""
 waitKey():
    o waitKey(0) will display the window infinitely until any keypress.
    o waitKey(n) will display a frame for n ms, after which display will be automatically closed.

"""


# cv2.waitKey(0)
# cv2.destroyAllWindows() # if we didn't add this and we showed an image after the waitKey all the old windows won't be closed

# cv2.imshow('img3', img)
# cv2.waitKey(0)

# ------------------------------ end intro to opencv gui + drawing  ----------------------------------------------


# ********************************** Region of image (ROI) *********************************************

# img = cv2.imread('/home/mohamed/Pictures/trees (copy).jpg', cv2.IMREAD_UNCHANGED)
# img2 = cv2.imread('/home/mohamed/Pictures/trees (copy).jpg', cv2.IMREAD_UNCHANGED)
# pixel = img[55,55] # access a specific pixel (x,y) position
# print(pixel)
# img[5, 5] = [0, 0, 0]


""" coloring a specific area of pixels using loops  """
# for i in range(500,600):
#     for j in range(500,600):
#         img[i,j] = [0,255,0]

"""   ROI(region of an image) : sub image of an image  """
"""   using slicing instead of looping through the img to set the pixels to a specific color (slicing  means taking elements from one given index to another given index)  """

# img2[500:600, 500:600] = [0,0,255]


""" copying a specific area of the image and pasting it some place in the image """

# image_copy = img[100:500, 100:500]
# img[0:400, 0:400] = image_copy # notice that it's exactly like the number of pixels i took in the previous line because i reserved this amount only
# cv2.imshow('img', img)
# cv2.imshow('img2', img2)
# cv2.waitKey(0)
#
# cv2.destroyAllWindows()


# ********************************** End of ROI *********************************************

# --------------------------------------------- Adding Images ----------------------------------------------

# the 2 images must be of same size
# img1 = cv2.imread('/home/mohamed/PycharmProjects/tkinter_delete/images/star-1.jpg', cv2.IMREAD_UNCHANGED)
# img2 = cv2.imread('/home/mohamed/PycharmProjects/tkinter_delete/images/dot.jpg', cv2.IMREAD_UNCHANGED)
#
# disease = img1 + img2 # add the star and the diamond together and the result will be a diamond shape in the star
# disease2 = img1 - img2 # notice that when you remove the diamond(second image) from the star(first image) that it will leave an empty diamond hole.keep in mind that if you reverse the subtraction of images img2 - img1 it will differ
# cv2.imshow("img1", img1)
# cv2.imshow("img2", img2)
#
# cv2.imshow('++', disease)
# # cv2.imshow('__', disease2)
# # cv2.imshow("img1", img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

""" add images using another way """


"""

if we want to add two images but give different weights to each image we use addWeighted
so that it gives a feeling of blending or transparency try the examples below to understand 

addWeighted: 
    o what does it do ? it blends two images together with the same size
    o params : 
        o img1
        o img1 weight 
        o img2 
        o img2 weight 
        o gamma : it is a static weight that will be added to all the pixels of the image.
    o equation behind it : 
        * img = a . img1 + b . img 2 + y (where a is the weight for first image and b is the weight for second image(weights ranges from 0 to 1) and y is the gamma value )

"""
# img1 = cv2.imread('/home/mohamed/PycharmProjects/tkinter_delete/images/1.png', cv2.IMREAD_UNCHANGED)
# img2 = cv2.imread('/home/mohamed/PycharmProjects/tkinter_delete/images/2.png', cv2.IMREAD_UNCHANGED)

# weighted = cv2.addWeighted(img1, 0.9, img2, 0.1, 10)

# cv2.imshow('weighted', weighted)
# cv2.imshow('img1', img1)
# # cv2.imshow('img2', img2)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# --------------------------------------------- End of Adding Images ----------------------------------------------

# ----------------------------------- Applying blurring effects ------------------------------------

# img = cv2.imread('/home/mohamed/Pictures/trees (copy).jpg', cv2.IMREAD_UNCHANGED)

# print(img.shape) # this will print the height(number of rows) and width(number of columns) and number of channels

"""
explanation of channels in opencv : 
    o So as OpenCV is an image processing Library, So A given image can be assumed as 2D matrix with each element as a pixel. 
      Now since there are various types of image formats like Gray, RGB or RGBA, etc. each format is different as to how many 
      colors it(pixel) can support. For example the pixels of Gray image take values in range 0-255 so to represent each gray 
      pixel we need single uchar(unsigned char) value, so it has single channel, similarly the pixels of RGB image can take values from 
      0-16777216 and to represent each RGB pixel, we need 3 uchar values, (256^3 = 16777216), hence it is 3 channels, similarly 
      RGBA has 4 channels, the last channel is used for storing the alpha(transparency) value.
"""


# kernel = np.ones((5,5), np.float32) / 25   # generate a kernel of ones with type float

# print(kernel)


""" apply our kernel to the image """
# smoothed = cv2.filter2D(img, -1, kernel) # the second param is called the depth of dest img it has information about what kinds of data stored in an image and If you use -1, the result (destination) image will have the same depth as the input (source) image.


# gaussian = cv2.GaussianBlur(img, (15,15), 0)

# median = cv2.medianBlur(img, 5)
# blur = cv2.blur(img, (5,5))

# cv2.imshow('img', img)
# cv2.imshow('smoothed', smoothed)
# cv2.imshow('gaussian', gaussian)
# cv2.imshow('median', median)
# cv2.imshow('mean', blur)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ----------------------------------- End of Applying blurring effects------------------------------------




# ------------------------------------------------ canny filter ---------------------------------------------
# img = cv2.imread('/home/mohamed/Pictures/trees (copy).jpg', cv2.IMREAD_UNCHANGED)

# canny = cv2.Canny(img,200,800) # img, threshold 1, threshold 2

# cv2.imshow('img', img)
# cv2.imshow('canny', canny)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# ----------------------------------------- End of canny ----------------------------------------------------------------------------



# ----------------------------------------- translating ----------------------------------------------------------------------------


# img = cv2.imread('/home/mohamed/Pictures/trees (copy).jpg', cv2.IMREAD_UNCHANGED)

# height, width =img.shape[:2] # getting the first 2 elements only which is height(number of rows), width(number of columns)
# print(img.shape[:2])
# T = np.float32([[1,0, 400],[0, 1, 50]]) # create the transformation matrix as floats
# translated = cv2.warpAffine(img, T, (width, height)) # apply the transformation to the img it takes the following params:  img, transformation matrix, tuple of (width, height)
# cv2.imshow('img', img)
# cv2.imshow('translated', translated)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ----------------------------------------- End of translating ----------------------------------------------------------------------------


# ----------------------------------------- rotating ----------------------------------------------------------------------------

# img = cv2.imread('/home/mohamed/Pictures/trees (copy).jpg', cv2.IMREAD_UNCHANGED)

# rotated_image = cv2.rotate(img, cv2.cv2.ROTATE_180)

# cv2.imshow('img', img)
# cv2.imshow('rotated', rotated_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

""" we could use the same function which we used for translating warpAffine to apply the rotation matrix like the example below """

# img = cv2.imread('/home/mohamed/Pictures/trees (copy).jpg', cv2.IMREAD_UNCHANGED)

# width, height = img.shape[:2]

""" 

cv2getRotationMatrix2D:
    what does it do ? gets the rotation matrix 
    params : 
        o the width, height ( we divided them by 2 to rotate n degree by the center )  
        o the degree of rotating.
        o the scale if we increase it it will scale the image up(zoom in).
 
 """

# rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)

# rotated_image = cv2.warpAffine(img, rotation_matrix, (width, height))

# cv2.imshow('img', img)
# cv2.imshow('rotated', rotated_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




# # -----------------------------------------End of rotating ----------------------------------------------------------------------------

# ----------------------------------------- scaling ----------------------------------------------------------------------------

img = cv2.imread('/home/mohamed/Pictures/trees (copy).jpg', cv2.IMREAD_UNCHANGED)

"""
to scale an image we use resize(). resize has 2 different modes for resizing the image.:
    o A fixed output size can be specified in the 2nd parameter.
    o Scaling factor for each dimension can be specified using the fx and fy parameters which are used for calculating the output size.

Note: If both methods are used simultaneously, then fx and fy parameters are ignored. The output size parameter is mandatory 
for both cases. It means that if we want to use the scaling method,  we have to pass None in place of the output size parameter. 
None indicates that we do not want to use this parameter.


resize() params:
    o img : the image
    o the output size which we can set it to None if we don't want to use it 
    o the fx: A variable representing the scale factor along the horizontal axis.
    o the fy: A variable representing the scale factor along the vertical axis.
    o the interpolation : A variable representing interpolation method in other words it's a way through which images are scaled. There are many different types of
     interpolation methods you can pick one of the following(i am not gonna dive into the algorithm behind each one of them i am just showing them for you to let you know that they're there) :   
        * INTER_NEAREST – a nearest-neighbor interpolation
        * INTER_LINEAR – a bilinear interpolation (used by default)
        * INTER_AREA – resampling using pixel area relation. It may be a preferred method for image decimation, as it gives more free results. 
          But when the image is zoomed, it is similar to the INTER_NEAREST method.
        * INTER_CUBIC – a bicubic interpolation over 4×4 pixel neighborhood

Simple Notes about the interpolation methods : 
    o if you are enlarging the image, you should prefer to use INTER_LINEAR or INTER_CUBIC interpolation. 
    o if you are shrinking the image, you should prefer to use INTER_AREA interpolation.
    o Cubic interpolation is computationally more complex, and hence slower than linear interpolation. 
      However, the quality of the resulting image will be higher.
"""


# scaled_down_with_specific_interpolation = cv2.resize(img, None, fx= 0.75, fy=0.75, interpolation= cv2.INTER_AREA) # scale in the x, y
# scaled_down = cv2.resize(img, None, fx= 0.75, fy=0.75) # scale in the x, y

# scaled_down_without_fx_fy = cv2.resize(img, (80, 80))
# scaled_up = cv2.resize(img, None, fx= 2, fy=2)


"""
another way to scale is by using pryUp or pryDown
in the example below i am scaling the same image down for many times then i scaled up one time only
"""


# small = cv2.pyrDown((img))
# small_2 = cv2.pyrDown((small))
# small_3 = cv2.pyrDown((small_2))
# large = cv2.pyrUp((img))
# cv2.imshow('img', img)
# cv2.imshow('scaled_down', scaled_down)
# cv2.imshow('scaled_down', scaled_down_without_fx_fy)
# cv2.imshow('scaled_down', scaled_down_with_specific_interpolation)
# cv2.imshow('scaled_up', scaled_up)
# cv2.imshow('small', small)
# cv2.imshow('small2', small_2)
# cv2.imshow('small3', small_3)
# cv2.imshow('large', large)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# -----------------------------------------End of scaling ----------------------------------------------------------------------------

# ----------------------------------------- cropping ----------------------------------------------------------------------------

# img = cv2.imread('/home/mohamed/Pictures/trees (copy).jpg', cv2.IMREAD_UNCHANGED)
# height, width = img.shape[:2]

# """ cropping from .25 to .75 of the image and then showing the cropped version """

# start_row, start_col = int(height * 0.25), int(width * 0.25)
# end_row, end_col = int(height * 0.75), int(width * 0.75)
# cropped = img[start_row:end_row, start_col:end_col]
# cv2.imshow('img', img)
# cv2.imshow('cropped', cropped)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# -----------------------------------------End of cropping ----------------------------------------------------------------------------







