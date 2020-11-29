import numpy as np
import cv2


# ----------------------------------------- reading a video ----------------------------------------------------------------------------


# 0 means the first camera in your computer if you have other cameras try 1 and etc.. 
# cap = cv2.VideoCapture(0)

# reading a video on your computer
# cap = cv2.VideoCapture('videoURL.format')

# while(True):
    # Capture frame-by-frame
    # ret, frame = cap.read()

    # Our operations on the frame comes here
    # Display the resulting frame
    # blurred = cv2.blur(frame, (10,10))

    # cv2.imshow('frame',frame)
    # cv2.imshow('blur',blurred)

    # quit when you click q
    # if cv2.waitKey(1) & 0xff == ord('q'):
    #     break

# When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()


# ----------------------------------------- End of reading a video ----------------------------------------------------------------------------




# ----------------------------------------- writing a video ----------------------------------------------------------------------------

# cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')

 # VideoWriter (const String &filename, int fourcc, double fps, Size frameSize)
# out = cv2.VideoWriter('output.avi',fourcc, 100.0, (640,480))

# while(cap.isOpened()):
    # ret, frame = cap.read()
    # if ret==True:

"""
The image is flipped according to the value of flipCode as follows:
    o flipcode = 0: flip vertically
    o flipcode > 0: flip horizontally
    o flipcode < 0: flip vertically and horizontally
        
"""
        # frame = cv2.flip(frame,0)

        # write the flipped frame
        # out.write(frame)
        # cv2.imshow('frame',frame)

        # if cv2.waitKey(1) & 0xff == ord('q'):
        #     break
    # else:
    #     break

# Release everything if job is finished
# cap.release()
# out.release()
# cv2.destroyAllWindows()
# # -----------------------------------------End of writing a video ----------------------------------------------------------------------------

