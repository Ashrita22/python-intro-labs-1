from tkinter import *

size_of_board = 600
number_of_dots = 6
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
rgb(70, 80, 0)
dot_color = '#7BC043' #r123, g192, b 43
player1_color = '#0492CF' #A0DDFF
player1_color_light = '#67B0CF' #758ECD
player2_color = '#EE4035' #C1CEFE
Green_color = '#7BC043' #7189FF
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
canvas.create_line(50, 50, 550, 50)