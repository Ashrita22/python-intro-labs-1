from tkinter import *

size_of_board = 600
number_of_dots = 6
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
#rgb(70, 80, 0)
dot_color = '#7BC043' #r123, g192, b 43
player1_color = '#A0DDFF' #A0DDFF
player1_color_light = '#758ECD' #758ECD
player2_color = '#C1CEFE' #C1CEFE
Green_color = '#7189FF' #7189FF
distance_between_dots = size_of_board / number_of_dots
dots_width = (1/4 * (size_of_board / number_of_dots))
edge_width = distance_between_dots / 10
#A0DDFF = Uranian Blue
#758ECD = Glaucous
#C1CEFE = Lavender Blue
#7189FF = Cornflower Blue
window = Tk()
window.title('Dots and Line Game')
canvas = Canvas(window, width=size_of_board, height=size_of_board)
canvas.pack()
window.mainloop(30)
#1st row
'''canvas.create_line(50, 50, 550, 50, fill="gray", dash=(2, 2))
#2nd row
canvas.create_line(50, 150, 550, 150, fill="gray", dash=(2,2))
#3rd row
canvas.create_line(50, 250, 550, 250, fill="gray", dash=(2,2))
#4th row
canvas.create_line(50, 350, 550, 350, fill="gray", dash=(2,2))
#5th row
canvas.create_line(50, 450, 550, 450, fill="gray", dash=(2,2))
#6th row
canvas.create_line(50, 550, 550, 550, fill="gray", dash=(2,2))

#1st column
canvas.create_line(50, 50, 50, 550, fill="gray", dash=(2,2))
#2nd column
canvas.create_line(150, 50, 150, 550, fill="gray", dash=(2,2))
#3rd column
canvas.create_line(250, 50, 250, 550, fill="gray", dash=(2,2))
#4th column
canvas.create_line(350, 50, 350, 550, fill="gray", dash=(2,2))
#5th column
canvas.create_line(450, 50, 450, 550, fill="gray", dash=(2,2))
#6th column
canvas.create_line(550, 50, 550, 550, fill="gray", dash=(2,2))'''

for i in range (50, 650, 100):
  canvas.create_line(50, i, 550, i, fill="gray", dash=(2,2))
  canvas.create_line(i, 50, i, 550, fill="gray", dash=(2,2))

for i in range(6):
  for j in range(6):
    start_x = i * 100 + 50
    end_x = j * 100 + 50
    canvas.create_oval(start_x - dots_width/2, end_x - dots_width/2, start_x + dots_width/2, end_x + dots_width/2, fill=dot_color, outline=dot_color)