# ------------------------------------------------- Start of Lab  -----------------------------------------------------------------------------------

# course github repo : https://github.com/ACUTeaching/CSC414
					  # -------------------------------------	



# python3 tkinter lab


import  tkinter as tk




# ----------------------------------------- creating a window ----------------------------------------------------------------------------


# create a window in tkinter ( the main window ) an instance of Tk class. Some people call the instance variable root and others call it window 
# you can call whatever you like but just letting you know
root = tk.Tk()

# set title of window
root.title("hello")

# set width and height and positioning of window
# root.geometry("500x500+800+600") # size of window 500x500, position +800+600
# root.geometry("+800+600")
root.geometry("500x500")

# ----------------------------------------- End of creating a window ----------------------------------------------------------------------------


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# ----------------------------------------- geometry managers ----------------------------------------------------------------------------------




# ----------------------------------------- pack ---------------------------------------------------------------------------------------------


# what are the widgets ? 
	# Tkinter exposes many classes. These are known as widgets. A widget is typically any part of the application that 
	# needs to be drawn onto the screen, including the main window, labels, buttons, etc..



# it's problem that the widgets depends on the order in which it's called 



# .pack() on it's own will add elements by the order in which they were added 

label = tk.Label(text= "Hello, Tkinter", foreground="#eee", background="gray")
label_2 = tk.Label(text= "Hello2", foreground="#eee", background="gray")

# label_2.pack()
# label.pack()


# pack important keywords : 
	# 1) fill: you position by horizontal and vertical axis (x,y)
	# 2) side : you position by the TOP, BOTTOM, LEFT, RIGHT
	# 3) expand: True or False (the element expands by expanding the window)


#============================= fill =================================================

# label.pack(fill= tk.X) # responsive by default
# label.pack(fill= tk.Y)
# label.pack(fill= tk.Y, expand=1) # responsive with the expand
# label.pack(fill=tk.BOTH, expand=True)

#============================= fill =================================================




#============================= side =================================================

# when you want to set the side that you want tkinter sets to the top by default

# label.pack(side= tk.TOP)
# label.pack(side= tk.BOTTOM)
# label.pack(side= tk.LEFT)
# label.pack(side= tk.RIGHT)


#============================= side =================================================


#============================= fill & side =================================================


# label.pack(fill=tk.Y, side=tk.RIGHT)

# fill the whole window and expand the component

# label.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


#============================= fill & side =================================================






# ----------------------------------------- End of pack --------------------------------------------------------------------------------------


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# ----------------------------------------- place --------------------------------------------------------------------------------------


# place control the precise location that a widget should occupy in a window or a frame by x, y ( the origin where x,y are 0) top left corner 
# of the frame or window

# label.place(x=0, y=0)

# ----------------------------------------- End of place --------------------------------------------------------------------------------------



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# ----------------------------------------- grid --------------------------------------------------------------------------------------

# .grid() works by splitting the window into rows and columns. You specify the location of a widget by calling .grid() and passing 
# the row and column indices to the row and column keyword arguments, respectively. Both row and column indices start at 0, so a row index of 1 and a column index of
#  2 tells .grid() to place a widget in the third column of the second row


# label.grid(row=2, column=4)


# for i in range(3):
# 	for j in range(3):
# 		# label2 = tk.Label(text="Row {}\n Column {}".format(i, j), width=10, height=10)
# 		label2 = tk.Label(text=f"Row {i}\n Column {j}", width=10, height=10)
# 		label2.grid(row= i, column= j)




# ----------------------------------------- End of grid --------------------------------------------------------------------------------------



# ----------------------------------------- End of geometry managers ----------------------------------------------------------------------------

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>






# ----------------------------------------- events  --------------------------------------------------------------------------------------------


# you must call the window.mainloop() to start the event loop during it
# your app checks if an event has occurred if so then some code can be executed in response
# you don't have to write code that checks for events
# you write functions in your code called event handlers for the events that you use in your app



# what's the definition of an event :
    # an event is any action that occurs during the event loop that might trigger some behavior in the application,
    # such as when a key or mouse button is pressed.When an event occurs, an event object is emitted, which means that an
    # instance of a class representing the event is instantiated. You don’t need to worry about creating these classes yourself.
    # Tkinter will create instances of event classes for you automatically.


# what does the mainloop() do :
    # It maintains a list of events that have occurred.
    # It runs an event handler any time a new event is added to that list.

# def printHello():
# 	print("Hello")


# btn = tk.Button(text="click me", bg="green", fg="#eee", command=printHello)

# btn.pack()

# ----------------------------------------- End of events  -------------------------------------------------------------------------------------



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




# ----------------------------------------- shapes ----------------------------------------------------------------------------------------------




# we create shapes in tkinter by using a widget called Canvas 

my_canvas = tk.Canvas(root, width=500, height= 500, bg="white")

my_canvas.pack()



# line

# my_canvas.create_line(x1, y1, x2, y2, fill="color")     o-----------------------------o        
 													  # (x1, y1)				   # (x2, y2)
# my_canvas.create_line(0, 100, 300, 100, fill="red")




# rectangle : x1, y1: Top Left and x2, y2: Bottom Right then it connects the points

     		# (x1, y1) o---------------
 					 # | 			  |
 					 # | 			  |
 		             # |			  |
 					 # ---------------o (x2, y2)
 				 					
# my_canvas.create_rectangle(10, 150, 400, 300, fill="green")



# triangle (polygon)

# points = [300,300, 500,300, 400,20] # {x1,y1}, {x2, y2}, {x3, y3}, {x_n, y_n....} 
# my_canvas.create_polygon(points)




# Oval: Somehow similar to the concept of drawing the rectangle 
my_canvas.create_oval(50, 150, 350, 100, fill="black")





# ----------------------------------------- End of shapes ----------------------------------------------------------------------------------------------

tk.mainloop() # making sure to keep the window open halts your program till you close the window








# ----------------------------------------- Tasks (easy tasks to get used to working with tkinter) ----------------------------------------------------------------------------------------------



# 1) create the following cross lines shape 


#   \  /
#    \/
#    /\
#   /  \


# 2) create the following triangle
   

		# --------------------
		# \                  /
		 # \                /
		  # \              /
		   # \            /
		    # \          /
		     # \        /
		      # \      / 
		       # \    /
                # \  /
                 # \/


# 3) create an oval 





# ------------------------------------------------- End of Lab  -----------------------------------------------------------------------------------

