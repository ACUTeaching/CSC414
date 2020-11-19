import cv2
import numpy as np
import matplotlib.pyplot as plt # a visualization library in python


# ----------------------------------------- brightness and contrast ----------------------------------------------------------------------------

# img = cv2.imread('/home/mohamed/Pictures/trees (copy).jpg', cv2.IMREAD_UNCHANGED)


"""
generate a matrix of ones based on the image shape and multiply it by 20 to be a matrix of twenties
if we want to increase the brightness we will increase the value of the 20 and if we want to
decrease it we will decrease the 20 value

"""

# M = np.ones(img.shape, dtype='uint8') * 20


# increase brightness
# added = cv2.add(img, M) # add the matrix of 20 s to the image

# decrease brightness
# subtracted = cv2.subtract(img, M) # subtract the matrix of 20 from the image

# cv2.imshow('img', img)
# cv2.imshow('added', added)
# cv2.imshow('subtracted', subtracted)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ----------------------------------------- End of brightness and contrast ----------------------------------------------------------------------------



# ----------------------------------------- arange & reshape & ravel --------------------------------------------------------------------------



""" arange """


"""

np.arange:
    o what does it do ? it creates an array for you within a specific range that you determine.
    o params arange(start, stop, step, dtype=None) : 
        - start : number, optional:
            * Start of interval. The interval includes this value. The default start value is 0.
        - stop : number : 
            * End of interval. The interval does not include this value,

        - stepnumber, optional : 
            * Spacing between values.
        - dtype : dtype : 
            * The type of the output array. If dtype is not given, infer the data type from the other input arguments.
    o return of arange : 
        - Array of evenly spaced values.


"""


""" arange examples """
# array = np.arange(3)
# print(array)
# array = np.arange(3.0)
# print(array)
#
# array = np.arange(3, 7)
# print(array)
#
# array = np.arange(3, 7, 2)
# print(array)
#
# array = np.arange(3.0, 4.0, 0.2, dtype=float)
# print(array)

# print("Original array : \n", array)


"""  reshape  """



"""     

np.reshape:
    o what does it do ? it is used to give a new shape to an array without changing its data.
    o params : 
        - a : array_like: 
            * Array to be reshaped.
        - new shape : int or tuple of ints:
            * the desired shape that we would like to give to an array.
            * for converting to shape of 2D or 3D array need to pass tuple.
            * For creating an array of shape 1D, an integer needs to be passed(-1).
        - order : {‘C’, ‘F’}, optional: order of elements
            * C : row wise
            * F : column wise
            * A : Read items from array based on memory order of items.
"""



# reshape example
# array = np.arange(1, 11).reshape(5, 2) # reshape to 2D ->  5 rows * 2 columns
# print(array)

"""

# Hints about reshape 

reshape(5, -1)
o the -1 i have passed to columns will make it guess the number of columns because we know the total number of generated elements 
  which is 10 and we have the number of rows which is 5 so it will easily guess that the number of columns is 2  


reshape(-1, 2)
o same as the above but this time it's the rows the -1 i passed to rows will make it guess the number of rows because we know the total number of generated elements 
  which is 10 and we have the number of columns which is 2 so it will easily guess that the number of columns is 5 


"""


""" Examples arrange with reshape(-1) """
# array = np.arange(1, 11).reshape(5, -1)
# array = np.arange(1, 11).reshape(-1, 2)
# array = np.arange(1, 11).reshape(-1) # reshape to 1D



"""  ravel """


"""

np.ravel(a, order='C') :
    o what does it do ? It returns a flattened 1D view of the input array.
    o params : 
        * a : array_like It can be a numpy array or any other array-like sequence like list. Elements from 
              it will be read based on given order.
        * order: The order in which items from numpy array will be used : 
            - ‘C’: row wise.
            - ‘F’: column wise.
            - ‘K’: Read items from array based on memory order of items.


Note: ravel does what the reshape(-1) do (turning the array into 1D)

"""


""" ravel examples """

# Create a 2D Numpy array
# arr_2d = np.array([ [0, 1, 2],
#                     [3, 4, 5],
#                     [6, 7, 8]])
# print('2D Numpy Array:')
# print(arr_2d)
#
#
# flat_array = np.ravel(arr_2d)
# print('Flattened view:')
# print(arr_2d.reshape(-1))
# print(flat_array)




# ----------------------------------------- End of arange & reshape & ravel --------------------------------------------------------------------------


# ----------------------------------------- histogram ----------------------------------------------------------------------------


# ----------------------------------------- Histogram using matplolib ----------------------------------------------------------------------------

# img = cv2.imread('/home/mohamed/Pictures/trees (copy).jpg', cv2.IMREAD_UNCHANGED)


# img_of_zeores = np.zeros((10, 10), dtype=int)


"""   

iterating over the image of zeroes and at each ith row position and from 0:9 columns we set the values to 
the changing variable x which changes by 50 each time just to make the same frequency for each element in the x axis. 

"""

# increaseBy = 0

# for i in range(10):
#     img_of_zeores[i, 0:10] = increaseBy
#     increaseBy += 50


"""

o params when drawing the histogram using matplotlib (note : these are the main params there are other params that can also be provided in here but i didn't cover them you can look in the docs of opencv to check them out):
    * flattened 1D array using ravel.
    * bins : size 
    * the range : upper and lower bound  

"""

# plt.hist(img_of_zeores.ravel(), 256, [0,256])
# plt.hist(img.ravel(), 256, [0,256])
# plt.show() # show the window
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ----------------------------------------- End of Histogram using matplolib ----------------------------------------------------------------------------

# ----------------------------------------- Histogram using opencv ----------------------------------------------------------------------------

# img = cv2.imread('/home/mohamed/Pictures/trees (copy).jpg', cv2.IMREAD_UNCHANGED)


# color = ('b', 'g', 'r') # cause we want to draw histogram for each channel



"""

why we have used enumerate in the for loop below ?
    o A lot of times when dealing with iterators, we also get a need to keep a count of iterations.
    Python eases the programmers’ task by providing a built-in function enumerate() for this task.
    Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
    This enumerate object can then be used directly in for loop

so basically what we did was when we're iterating we put the current counter in i and the color attached to it in col

ex: 
0, "B"  # i : 0 , col : B
1, "G"  # i : 1 , col : G
2, "R"  # i : 2 , col : R

    o params of enumerate :
        - Iterable: any object that supports iteration
        - Start: the index value from which the counter is
          to be started, by default it is 0

"""

# for i, col in enumerate(color):
"""
    cv.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])

        parms:
            o images : it is the source image of type uint8 or float32. it should be given in square brackets, ie, "[img]".
            o channels : it is also given in square brackets. It is the index of channel for which we calculate histogram. For example, if input is grayscale image, its value is [0]. For color image, you can pass [0], [1] or [2] to calculate histogram of blue, green or red channel respectively.
            o mask : mask image. To find histogram of full image, it is given as "None". But if you want to find histogram of particular region of image, you have to create a mask image for that and give it as mask.
            o histSize : this represents our BIN count. Need to be given in square brackets. For full scale, we pass [256].
            o ranges : this is our RANGE. Normally, it is [0,256].

"""
    # histogram = cv2.calcHist([img], [i], None, [256], [0, 256])
    # plt.plot(histogram, color= col) # plot histogram for the current color
    # plt.xlim([0, 256]) # set x axis limit from 0 to 256 in this

# plt.show() # show the window



# ----------------------------------------- End of Histogram using opencv ----------------------------------------------------------------------------


# ----------------------------------------- End of histogram ----------------------------------------------------------------------------





