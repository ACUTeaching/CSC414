from moviepy.editor import *
import pygame


# a function to play a video using pygame library uncomment it to use it

"""
def play_video(clip, caption):
    pygame.display.set_caption(caption)
    clip.preview()
    pygame.quit()
"""




"""
We will load the video, and we will cut a clip from the whole video then the video will be rotated upside down, 
in this example, there is no need for ImageMagick installation.

"""

# loading video
# clip = VideoFileClip("fell_asleep.mp4")

# clipping of the video
# getting the first 10 seconds only from 0th second to the 10th second
# clip = clip.subclip(0, 10)

""" another method to set the start """
# clip = clip.set_start(t=5) # start at the 5th second


# rotatng video by 180 degree
# clip = clip.rotate(180)

# Reduce the audio volume (volume x 0.5)
# clip = clip.volumex(0.5)

""" play a video by using ipython in anaconda => jupyter notebook"""
# clip.ipython_display(width = 280)


"""  play a video by using pygame """
# play_video(clip, "fell asleep")





"""

We will load the video and we will cut a clip from the whole video then we will add text in the video, 
in this example we have to install ImageMagick otherwise it will not work.

"""

# loading video
# clip = VideoFileClip("fell_asleep.mp4")

# clip = clip.subclip(0, 10)

# clip = clip.volumex(0.8)

# Generate a text clip
# txt_clip = TextClip("test", fontsize = 70, color = 'white')

# setting position of text in the center and duration will be 10 seconds
# txt_clip = txt_clip.set_pos('center').set_duration(10)

# Overlay the text clip on the first video clip
# video = CompositeVideoClip([clip, txt_clip])

# video.ipython_display(width = 280)



""" composing the same or different videos on each other """

# loading video the video and getting only the first 5 seconds
# clip1 = VideoFileClip("fell_asleep.mp4").subclip(0, 5)

# rotating clip1 by 90 degree to get the clip2
# clip2 = clip1.margin(40).set_start(3)

# rotating clip1 by 180 degree to get the clip3
# clip3 = clip1.rotate(180).set_start(6)

# creating a composite video
# final = CompositeVideoClip([clip2, clip1, clip3])

# showing final clip
# final.ipython_display(width = 480)




""" concatenate videos to each others and saving the output to a file  """

# clip_1= VideoFileClip("fell_asleep.mp4")
# clip_2= VideoFileClip("fell_asleep.mp4")

"""
TO join the video's i.e. concatenate the videos'
use function concatenate_videoclips(list_of_clips_to_mearged)
syntax:
variable_to_hold_mearged_video= moviepy.editor.concatenate_videclips([video_1,Video_2,. . .])
"""
# Merged_video=concatenate_videoclips([clip_1,clip_2])

# Saving File as output.mp4  in same folder
# libx264 is encoding lib for creating video stream(H.264)
# Merged_video.write_videofile("Output.mp4",codec='libx264')
# print("Done")



